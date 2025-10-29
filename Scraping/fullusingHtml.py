import re
import csv
import logging
from datetime import datetime
from typing import Optional, Dict, List

from lxml import html
from pymongo import MongoClient
from playwright.sync_api import sync_playwright

# ---------------- Logging ----------------
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def checkpoint(name: str, data: dict = None):
    log.info("[CHECKPOINT] %s", name)
    if data:
        log.info("%s", data)

# ---------------- Playwright Setup ----------------
def fetch_page(url: str, timeout=60000) -> Optional[str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120 Safari/537.36"
        ))
        try:
            page.goto(url, timeout=timeout, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            html_content = page.content()
            return html_content
        except Exception as e:
            log.error("Playwright fetch failed: %s", e)
            return None
        finally:
            browser.close()

# ---------------- Product Extractor ----------------
def extract_product(html_bytes: str, url: str) -> Dict:
    tree = html.fromstring(html_bytes)

    def text_or_none(xpath: str) -> Optional[str]:
        el = tree.xpath(xpath)
        return el[0].strip() if el else None

    def all_text(xpath: str) -> List[str]:
        return [e.strip() for e in tree.xpath(xpath) if e.strip()]

    def extract_table(xpath: str) -> Dict:
        out = {}
        rows = tree.xpath(xpath)
        for row in rows:
            key = "".join(row.xpath(".//th//text()")).strip()
            val = "".join(row.xpath(".//td//text()")).strip()
            if key and val:
                out[key] = val
        return out

    product = {
        "url": url,
        "title": text_or_none('//span[@id="productTitle"]/text()'),
        "price": (
            text_or_none('//span[@id="priceblock_ourprice"]/text()')
            or text_or_none('//span[@id="priceblock_dealprice"]/text()')
            or text_or_none('//span[@class="a-price-whole"]/text()')
        ),
        "brand": text_or_none('//a[@id="bylineInfo"]/text()'),
        "category": " > ".join(all_text('//a[@class="a-link-normal a-color-tertiary"]//text()')),
        "about": " ".join(all_text('//div[@id="feature-bullets"]//li//text()')),
        "availability": text_or_none('//div[@id="availability"]//span/text()'),
        "rating": text_or_none('//span[@id="acrPopover"]/@title'),
        "review_count": text_or_none('//span[@id="acrCustomerReviewText"]/text()'),
        "images": tree.xpath('//div[@id="altImages"]//img/@src'),
        "product_info": extract_table('//table[@id="productDetails_detailBullets_sections1"]//tr'),
        "technical_details": extract_table('//table[@id="productDetails_techSpec_section_1"]//tr'),
        "additional_info": extract_table('//table[@id="productDetails_additionalInfo"]//tr'),
        "_extracted_at": datetime.utcnow().isoformat()
    }
    return product

# ---------------- Search Results ----------------
def extract_asins_from_search(html_bytes: str) -> List[str]:
    tree = html.fromstring(html_bytes)
    asins = tree.xpath('//div[@data-asin and @data-asin!=""]/@data-asin')
    return asins[:30]  # limit 30 products for preview

# ---------------- MongoDB Save ----------------
def save_to_mongo(product: dict):
    client = MongoClient("mongodb://localhost:27017")
    db = client["products_db"]
    coll = db["amazon_products_shampoo_for_dry_hair"]
    coll.update_one({"url": product["url"]}, {"$set": product}, upsert=True)

# ---------------- CSV Save ----------------
def save_to_csv(products: List[dict], filename="amazon_preview.csv"):
    if not products:
        return
    keys = set()
    for p in products:
        keys.update(p.keys())
    keys = list(keys)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)

# ---------------- Main ----------------
def main():
    keyword = "shampoo for dry hair"   # 🔑 yaha tum apna keyword change kar sakte ho
    search_url = f"https://www.amazon.in/s?k={keyword.replace(' ', '+')}"

    checkpoint("Fetching search results", {"keyword": keyword})
    search_html = fetch_page(search_url)
    if not search_html:
        log.error("Failed to fetch search results")
        return

    asins = extract_asins_from_search(search_html)
    checkpoint("Extracted ASINs", {"count": len(asins)})

    products = []
    for asin in asins:
        product_url = f"https://www.amazon.in/dp/{asin}"
        prod_html = fetch_page(product_url)
        if not prod_html:
            continue
        product = extract_product(prod_html, product_url)
        products.append(product)
        save_to_mongo(product)
        checkpoint("Saved product", {"asin": asin})

    save_to_csv(products)
    log.info("Saved %d products to MongoDB and CSV", len(products))

if __name__ == "__main__":
    main()
