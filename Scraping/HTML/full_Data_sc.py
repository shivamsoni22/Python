import re
import csv
import logging
from datetime import datetime
from typing import Optional, List, Dict

from lxml import html
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from playwright.sync_api import sync_playwright

# ---------------- Logging Setup ----------------
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def checkpoint(name: str, data: dict = None):
    log.info("[CHECKPOINT] %s", name)
    if data:
        log.info("%s", data)

# ---------------- Playwright Fetch ----------------
def fetch_playwright(url: str, timeout=60000) -> Optional[str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120 Safari/537.36"
        )
        try:
            checkpoint("Navigating to URL", {"url": url})
            page.goto(url, timeout=timeout, wait_until="domcontentloaded")
            page.wait_for_timeout(2000)
            content = page.content()
            return content
        except Exception as e:
            log.error("Playwright fetch failed: %s", e)
        finally:
            browser.close()
    return None

# ---------------- Extract ASINs from search ----------------
def extract_asins_from_search(html_content: str) -> List[str]:
    tree = html.fromstring(html_content)
    asin_nodes = tree.xpath('//div[@data-asin and @data-component-type="s-search-result"]/@data-asin')
    return [asin for asin in asin_nodes if asin.strip()]

# ---------------- Extract product info ----------------
def extract_product(html_bytes: bytes, url: str) -> Dict:
    checkpoint("Parsing HTML content")
    tree = html.fromstring(html_bytes)

    def text_or_none(xpath: str) -> Optional[str]:
        el = tree.xpath(xpath)
        return el[0].strip() if el else None

    def all_text(xpath: str) -> List[str]:
        return [e.strip() for e in tree.xpath(xpath) if e.strip()]

    product = {
        "url": url,
        "title": text_or_none('//span[@id="productTitle"]/text()'),
        "price": text_or_none('//span[@id="priceblock_ourprice"]/text()')
                 or text_or_none('//span[@id="priceblock_dealprice"]/text()')
                 or text_or_none('//span[@class="a-price-whole"]/text()'),
        "asin": text_or_none('//th[text()="ASIN"]/following-sibling::td/text()')
                or url.split("/")[-1],
        "brand": text_or_none('//a[@id="bylineInfo"]/text()'),
        "description": " ".join(all_text('//div[@id="feature-bullets"]//li//text()')),
        "rating": text_or_none('//span[@id="acrPopover"]/@title'),
        "review_count": text_or_none('//span[@id="acrCustomerReviewText"]/text()'),
        "availability": text_or_none('//div[@id="availability"]//span/text()'),
        "_extracted_at": datetime.utcnow().isoformat()
    }
    checkpoint("Extracted product fields", product)
    return product

# ---------------- Mongo Save ----------------
def save_product(coll, prod: dict):
    identifier = {"url": prod["url"]}
    checkpoint("Saving product to MongoDB", identifier)
    try:
        res = coll.update_one(identifier, {"$set": prod}, upsert=True)
        log.info("MongoDB result matched=%s modified=%s upserted_id=%s",
                 res.matched_count, res.modified_count, res.upserted_id)
    except DuplicateKeyError as e:
        log.warning("Duplicate key detected: %s", e)

# ---------------- CSV Save ----------------
def save_to_csv(filename: str, products: List[Dict]):
    keys = set()
    for p in products:
        keys.update(p.keys())
    keys = list(keys)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for p in products:
            writer.writerow(p)

# ---------------- Main ----------------
def main():
    keyword = "face wash"  # 👈 yaha apna keyword change karo
    max_products = 500
    base_url = f"https://www.amazon.in/s?k={keyword.replace(' ', '+')}&page="

    checkpoint("Connecting to MongoDB", {
        "uri": "mongodb://localhost:27017",
        "db": "products_db",
        "collection": "amazon_products"
    })

    client = MongoClient("mongodb://localhost:27017")
    db = client["products_db"]
    coll = db["amazon_products_face_wash"]

    all_products = []
    page_num = 1
    seen_asins = set()

    while len(all_products) < max_products:
        search_url = base_url + str(page_num)
        html_content = fetch_playwright(search_url)
        if not html_content:
            break

        asins = extract_asins_from_search(html_content)
        if not asins:
            break

        for asin in asins:
            if asin in seen_asins:
                continue
            seen_asins.add(asin)

            product_url = f"https://www.amazon.in/dp/{asin}"
            prod_html = fetch_playwright(product_url)
            if not prod_html:
                continue

            product = extract_product(prod_html.encode("utf-8"), product_url)
            save_product(coll, product)
            all_products.append(product)

            if len(all_products) >= max_products:
                break

        page_num += 1

    # Save all products to CSV
    save_to_csv("amazon_products.csv", all_products)
    log.info("Scraping finished. Total products: %s", len(all_products))

if __name__ == "__main__":
    main()
