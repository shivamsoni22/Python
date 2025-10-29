from email.header import decode_header
from email.quoprimime import header_decode

import requests
import time
import random
import pandas as pd
import pymongo
from bs4 import BeautifulSoup
from dns.edns import CookieOption
from dns.rdtypes.ANY.HINFO import HINFO
from dns.resolver import NXDOMAIN
from pandas.core.internals import ArrayManager
from pymongo import MongoClient
from pymongo.asynchronous.pool import AsyncConnection
from requests.adapters import HTTPAdapter, Retry
from selenium.webdriver.common.devtools.v137.accessibility import AXValue

from Scraping.HTML.findDataUsinghtmlXpath import headers

# ==============================
#  SETUP
# ==============================
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "teacollection"
COLLECTION_NAME = "products"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

session = requests.Session()
retries = Retry(total=3, backoff_factor=2, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json"
}

# ==============================
#  1️⃣ FETCH PRODUCTS FROM ALGOLIA
# ==============================

payload = {
    "requests": [
        {
            "indexName": "teacollection_products",
            "params": "query=&hitsPerPage=20"
        }
    ]
}

print("Fetching product list from Algolia...")
resp = session.post( json=payload, headers=HEADERS, timeout=15)
resp.raise_for_status()

products_data = resp.json()["results"][0]["hits"][:20]
print(f"✅ Retrieved {len(products_data)} products")

# ==============================
#  2️⃣ SCRAPE EACH PRODUCT PAGE
# ==============================
records = []

for i, product in enumerate(products_data, 1):
    product_url = f"https://www.teacollection.com/product/{product.get('sku', '')}.html"
    print(f"\n[{i}] Scraping: {product_url}")

    try:
        res = session.get(product_url, headers=HEADERS, timeout=15)
        res.raise_for_status()

        # Save HTML locally
        html_filename = f"product_{i}_{product.get('sku', 'no_sku')}.html"
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(res.text)

        soup = BeautifulSoup(res.text, "html.parser")

        def safe_text(selector):
            el = soup.select_one(selector)
            return el.get_text(strip=True) if el else "n/a"

        title = safe_text("div.product-title h1 span")
        sku = safe_text("span.sku.hidden span")
        mrp_text = safe_text("p#store_price strike")
        selling_text = safe_text("p#store_price span:nth-of-type(2)")

        # Convert prices to numbers if possible
        def parse_price(text):
            try:
                return float(text.replace("$", "").strip())
            except:
                return None

        mrp = parse_price(mrp_text)
        selling = parse_price(selling_text)
        discount = round(mrp - selling, 2) if mrp and selling else "n/a"
        discount_percent = f"{round(((mrp - selling) / mrp) * 100, 1)}%" if mrp and selling else "n/a"

        reviews = safe_text("a#read-reviews")
        color = safe_text("span.selected-value")
        category = ", ".join([t.get_text(strip=True) for t in soup.select("div.breadcrumbs.container a span")]) or "n/a"
        favorites = safe_text("span.count")

        # Details sections
        def get_section(title_selector, content_selector):
            title = safe_text(title_selector)
            content = " ".join([t.get_text(strip=True) for t in soup.select(content_selector)]) or "n/a"
            return {title: content}

        description = get_section("li.description h2", "li.description div div")
        size = get_section("li.size h2", "li.size div p")
        features = get_section("li.features h2", "li.features div.contents ul li")
        shipping = get_section("li.shipping h2", "li.shipping div.contents div")

        record = {
            "title": title,
            "sku": sku,
            "mrp": mrp_text or "n/a",
            "selling_price": selling_text or "n/a",
            "discount_amount": discount,
            "discount_percent": discount_percent,
            "reviews": reviews,
            "color": color,
            "favorites": favorites,
            "category": category,
            "description": description,
            "size": size,
            "features": features,
            "shipping": shipping,
            "url": product_url,
        }

        # Save to MongoDB
        collection.update_one({"sku": sku}, {"$set": record}, upsert=True)
        records.append(record)

        # Polite random delay
        delay = random.uniform(2.0, 4.5)
        print(f"Waiting {delay:.1f}s before next request...")
        time.sleep(delay)

    except Exception as e:
        print(f"⚠️ Error fetching {product_url}: {e}")
        continue

# ==============================
#  3️⃣ PREVIEW RESULTS IN CONSOLE
# ==============================
df = pd.DataFrame(records)
print("\n=== DataFrame Preview ===")
print(df.head(10))














































