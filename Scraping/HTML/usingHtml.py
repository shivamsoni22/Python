# import re
# import json
# import logging
# from datetime import datetime
# from typing import Optional, List, Dict
#
# from lxml import html
# from pymongo import MongoClient
# from pymongo.errors import DuplicateKeyError
# from playwright.sync_api import sync_playwright
#
# # ---------------- Logging Setup ----------------
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s [%(levelname)s] %(message)s")
# log = logging.getLogger(__name__)
#
#
# def checkpoint(name: str, data: dict = None):
#     log.info("[CHECKPOINT] %s", name)
#     if data:
#         log.info("[CHECKPOINT] %s", json.dumps(data, indent=2, ensure_ascii=False))
#
#
# # ---------------- Playwright Fetch ----------------
# def fetch_playwright(url: str, timeout=60000, retries=3) -> Optional[bytes]:
#     for attempt in range(1, retries + 1):
#         checkpoint(f"Playwright Fetch Attempt {attempt}")
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)  # Debug के लिए False
#             page = browser.new_page(
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                            "AppleWebKit/537.36 (KHTML, like Gecko) "
#                            "Chrome/120 Safari/537.36",
#                 viewport={"width": 1280, "height": 800},
#                 java_script_enabled=True,
#             )
#             try:
#                 checkpoint("Navigating to URL", {"url": url})
#                 page.goto(url, timeout=timeout, wait_until="domcontentloaded")
#
#                 # Ensure product title loaded
#                 page.wait_for_selector("#productTitle", timeout=20000)
#
#                 content = page.content()
#                 checkpoint("Fetched HTML length", {"length": len(content)})
#
#                 with open("amazon_debug.html", "w", encoding="utf-8") as f:
#                     f.write(content)
#
#                 return content.encode("utf-8")
#             except Exception as e:
#                 log.error("Playwright fetch failed: %s", e)
#             finally:
#                 browser.close()
#     return None
#
#
# # ---------------- HTML Parser ----------------
# def extract_table(tree, heading: str) -> Dict[str, str]:
#     """Extracts key-value pairs from table under given heading"""
#     data = {}
#     section = tree.xpath(f'//h1[contains(text(),"{heading}")]/following::table[1]') \
#               or tree.xpath(f'//h2[contains(text(),"{heading}")]/following::table[1]')
#     if section:
#         rows = section[0].xpath(".//tr")
#         for row in rows:
#             key = "".join(row.xpath(".//th//text()")).strip(" :\u200e")
#             val = "".join(row.xpath(".//td//text()")).strip()
#             if key:
#                 data[key] = val
#     return data
#
#
# def extract_product(html_bytes: bytes, url: str) -> Dict:
#     checkpoint("Parsing HTML content")
#     tree = html.fromstring(html_bytes)
#
#     def text_or_none(xpath: str) -> Optional[str]:
#         el = tree.xpath(xpath)
#         return el[0].strip() if el else None
#
#     def all_text(xpath: str) -> List[str]:
#         return [e.strip() for e in tree.xpath(xpath) if e.strip()]
#
#     product = {
#         "url": url,
#         "title": text_or_none('//span[@id="productTitle"]/text()'),
#         "price": (
#             text_or_none('//span[@id="priceblock_ourprice"]/text()')
#             or text_or_none('//span[@id="priceblock_dealprice"]/text()')
#             or text_or_none('//span[@class="a-price-whole"]/text()')
#         ),
#         "asin": (
#             text_or_none('//th[contains(text(),"ASIN")]/following-sibling::td/text()')
#             or url.split("/")[-1].split("?")[0]
#         ),
#         "brand": text_or_none('//a[@id="bylineInfo"]/text()'),
#         "description": " ".join(all_text('//div[@id="feature-bullets"]//li//text()')),
#         "rating": text_or_none('//span[@id="acrPopover"]/@title')
#                   or text_or_none('//span[@id="acrPopover"]//text()'),
#         "review_count": text_or_none('//span[@id="acrCustomerReviewText"]/text()'),
#         "availability": text_or_none('//div[@id="availability"]//span/text()'),
#         "images": tree.xpath('//div[@id="altImages"]//img/@src'),
#         # Extra sections
#         "about_item": " ".join(all_text('//div[@id="feature-bullets"]//li//text()')),
#         "important_info": " ".join(all_text('//div[@id="importantInformation"]//text()')),
#         "product_description": " ".join(all_text('//div[@id="productDescription"]//p//text()')),
#         "product_information": extract_table(tree, "Product information"),
#         "technical_details": extract_table(tree, "Technical Details"),
#         "additional_information": extract_table(tree, "Additional Information"),
#         "product_details": extract_table(tree, "Product details"),
#         "best_sellers_rank": " ".join(all_text('//th[contains(text(),"Best Sellers Rank")]/following-sibling::td//text()')),
#         "customer_reviews": " ".join(all_text('//span[@data-asin and contains(@class,"reviewCount")]//text()')),
#         "seller_info": {
#             "ships_from": text_or_none('//div[@id="shipsFromSoldBy_feature_div"]//span[contains(text(),"Ships from")]/following-sibling::span/text()'),
#             "sold_by": text_or_none('//div[@id="shipsFromSoldBy_feature_div"]//a/text()'),
#         },
#         "payment_methods": " ".join(all_text('//div[@id="payMethods"]//text()')),
#         "_extracted_at": datetime.utcnow().isoformat()
#     }
#
#     checkpoint("Extracted product fields", product)
#     return product
#
#
# # ---------------- Mongo Save ----------------
# def clean_asin(asin: Optional[str]) -> Optional[str]:
#     if not asin:
#         return None
#     return re.sub(r"[^\w]", "", asin.strip())
#
#
# def save_product(coll, prod: dict):
#     if prod.get("asin"):
#         prod["asin"] = clean_asin(prod["asin"])
#
#     identifier = {}
#     if prod.get("asin"):
#         identifier["asin"] = prod["asin"]
#     elif prod.get("url"):
#         identifier["url"] = prod["url"]
#
#     checkpoint("Saving product to MongoDB", identifier)
#     try:
#         res = coll.update_one(identifier, {"$set": prod}, upsert=True)
#         log.info("MongoDB result matched=%s modified=%s upserted_id=%s",
#                  res.matched_count, res.modified_count, res.upserted_id)
#     except DuplicateKeyError as e:
#         log.warning("Duplicate key detected, retrying by URL only: %s", e)
#         res = coll.update_one({"url": prod["url"]}, {"$set": prod}, upsert=True)
#         log.info("Retry update result matched=%s modified=%s upserted_id=%s",
#                  res.matched_count, res.modified_count, res.upserted_id)
#
#
# # ---------------- Main ----------------
# def main():
#     url = "https://www.amazon.in/dp/B01CCGW4OE/?th=1"
#
#     html_bytes = fetch_playwright(url)
#     if not html_bytes:
#         log.error("Failed to fetch HTML")
#         return
#
#     product = extract_product(html_bytes, url)
#
#     # ✅ Preview JSON in console
#     print("\n========= SCRAPED PRODUCT DATA =========")
#     print(json.dumps(product, indent=2, ensure_ascii=False))
#     print("========================================\n")
#
#     checkpoint("Connecting to MongoDB", {
#         "uri": "mongodb://localhost:27017",
#         "db": "products_db",
#         "collection": "amazon_products"
#     })
#
#     client = MongoClient("mongodb://localhost:27017")
#     db = client["products_db"]
#     coll = db["amazon_products"]
#
#     save_product(coll, product)
#
#
# if __name__ == "__main__":
#     main()


