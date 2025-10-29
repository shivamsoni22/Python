# import os
# import time
# import random
# import requests
# import pandas as pd
# from pymongo import MongoClient
# from bs4 import BeautifulSoup
# import warnings
#
# warnings.filterwarnings("ignore", category=RuntimeWarning)
#
# # -------------------- MongoDB Configuration --------------------
# client = MongoClient("mongodb://localhost:27017/")
# db = client["tiffany_db"]
# collection = db["products"]
#
# # -------------------- Headers & API Config --------------------
# HEADERS = {
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Origin': 'https://www.tiffany.com',
#     'Referer': 'https://www.tiffany.com/',
#     'User-Agent': (
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#         'AppleWebKit/537.36 (KHTML, like Gecko) '
#         'Chrome/141.0.0.0 Safari/537.36'
#     ),
#     'content-type': 'application/x-www-form-urlencoded',
# }
#
# ALGOLIA_URL = (
#     "https://u9oxz6rbmd-dsn.algolia.net/1/indexes/*/queries"
#     "?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)"
#     "%3B%20Browser%20(lite)%3B%20Algolia%20Salesforce%20B2C%20(SFRA)"
#     "%20(v24.2.0)%3B%20instantsearch.js%20(4.80.0)%3B%20JS%20Helper%20(3.26.0)"
#     "&x-algolia-api-key=ce66200c6b0317e7a97579e4e04c0063"
#     "&x-algolia-application-id=U9OXZ6RBMD"
# )
#
# DATA = '{"requests":[{"indexName":"ecommerce_us_products__en_US","params":"clickAnalytics=true&facetFilters=%5B%5D&facets=%5B%22*%22%5D&filters=browseOnlineFrom.timestamp%20%3C%3D%201759833000%20AND%20browseOnlineTo.timestamp%20%3E%3D%201759833000%20AND%20categoryFilters%3Ajewelry_rings&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&maxValuesPerFacet=20&page=0"}]}'
#
# # -------------------- Helper Functions --------------------
# def safe_get(obj, path):
#     """Safely get nested fields from dict/list using dot notation."""
#     try:
#         for key in path.split('.'):
#             if isinstance(obj, list):
#                 obj = obj[int(key)]
#             else:
#                 obj = obj.get(key)
#         return obj if obj is not None else "N/A"
#     except Exception:
#         return "N/A"
#
#
# def save_product_html(url, code):
#     """Fetch and save product page HTML with retries."""
#     for attempt in range(3):
#         try:
#             response = requests.get(url, headers=HEADERS, timeout=20)
#             if response.status_code == 200:
#                 os.makedirs("tiffany_pages", exist_ok=True)
#                 file_path = os.path.join("tiffany_pages", f"{code}.html")
#                 soup = BeautifulSoup(response.text, "html.parser")
#                 with open(file_path, "w", encoding="utf-8") as f:
#                     f.write(soup.prettify())
#                 print(f"🟢 Saved HTML ({attempt+1} try): {file_path}")
#                 return
#             else:
#                 print(f"⚠️ Failed ({response.status_code}) for {code}, retrying...")
#         except Exception as e:
#             print(f"❌ HTML Save Error (try {attempt+1}) for {code}: {e}")
#             time.sleep(3)
#     print(f"⛔ Skipped HTML for {code} after 3 retries.")
#
#
# # -------------------- Fetch and Process --------------------
# print("🚀 Fetching up to 10 Tiffany products...")
#
# response = requests.post(ALGOLIA_URL, headers=HEADERS, data=DATA)
# print(f"🔗 Response Code: {response.status_code}")
#
# if response.status_code == 200:
#     data = response.json()
#     hits = data["results"][0]["hits"][:10]
#
#     final_data = []
#
#     for p in hits:
#         product_url = safe_get(p, "productUrl.canonicalUrl")
#         if not product_url.startswith("http"):
#             product_url = "https://www.tiffany.com" + product_url
#
#         item = {
#             "availableQuantity": safe_get(p, "availableQuantity"),
#             "isLowInventory": safe_get(p, "isLowInventory"),
#             "_tags": safe_get(p, "_tags"),
#             "itemMasterId": safe_get(p, "itemMasterId"),
#             "styleId": safe_get(p, "styleId"),
#             "level0Id": safe_get(p, "level0Id"),
#             "categories": safe_get(p, "categories"),
#             "motif": safe_get(p, "motif"),
#             "productType": safe_get(p, "productType"),
#             "family": safe_get(p, "family"),
#             "legalCollection": safe_get(p, "legalCollection"),
#             "hazardousMaterials": safe_get(p, "hazardousMaterials"),
#             "merchindisingCollection": safe_get(p, "merchindisingCollection"),
#             "materialSubType": safe_get(p, "materialSubType"),
#             "primaryGemstoneSpecies": safe_get(p, "primaryGemstoneSpecies"),
#             "bucketingMaterialSubType": safe_get(p, "bucketingMaterialSubType"),
#             "designerAndCollectionFilter": safe_get(p, "designerAndCollectionFilter"),
#             "primaryCategories": safe_get(p, "primaryCategories"),
#             "collection": safe_get(p, "collection"),
#             "brand": safe_get(p, "brand"),
#             "maxOrderQuantity": safe_get(p, "maxOrderQuantity"),
#             "designer": safe_get(p, "designer"),
#             "color": safe_get(p, "color"),
#             "baselineStrategy": safe_get(p, "baselineStrategy"),
#             "size": safe_get(p, "size"),
#             "urlImage": safe_get(p, "urlImage"),
#             "images": safe_get(p, "images"),
#             "description": safe_get(p, "description"),
#             "additionalSpecifications": safe_get(p, "additionalSpecifications"),
#             "manufacturerSkus": safe_get(p, "manufacturerSkus"),
#             "videos": safe_get(p, "videos"),
#             "productUrl": product_url,
#             "parentPrice": safe_get(p, "parentPrice"),
#             "variationsAvailable": safe_get(p, "variationsAvailable"),
#             "relativeUrls": safe_get(p, "relativeUrls"),
#         }
#
#         final_data.append(item)
#
#         # Save HTML Page
#         save_product_html(product_url, str(item["styleId"]))
#         time.sleep(random.uniform(2, 5))  # polite delay
#
#     # -------------------- Store in MongoDB --------------------
#     if final_data:
#         collection.insert_many(final_data)
#         print(f"\n✅ {len(final_data)} products inserted into MongoDB successfully!")
#
#         # -------------------- Preview Data --------------------
#         df = pd.DataFrame(final_data)
#         print("\n🧾 Data Preview:")
#         print(df.head(5))
#     else:
#         print("⚠️ No products found.")
# else:
#     print("❌ API Request Failed. Check headers or URL.")



import os
import time
import random
import requests
import pandas as pd
from pymongo import MongoClient
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# -------------------- MongoDB Configuration --------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["tiffany_db"]
collection = db["products"]

# -------------------- Headers & API Config --------------------
HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.tiffany.com',
    'Referer': 'https://www.tiffany.com/',
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/141.0.0.0 Safari/537.36'
    ),
    'content-type': 'application/x-www-form-urlencoded',
}

ALGOLIA_URL = (
    "https://u9oxz6rbmd-dsn.algolia.net/1/indexes/*/queries"
    "?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)"
    "%3B%20Browser%20(lite)%3B%20Algolia%20Salesforce%20B2C%20(SFRA)"
    "%20(v24.2.0)%3B%20instantsearch.js%20(4.80.0)%3B%20JS%20Helper%20(3.26.0)"
    "&x-algolia-api-key=ce66200c6b0317e7a97579e4e04c0063"
    "&x-algolia-application-id=U9OXZ6RBMD"
)

DATA = '{"requests":[{"indexName":"ecommerce_us_products__en_US","params":"clickAnalytics=true&facetFilters=%5B%5D&facets=%5B%22*%22%5D&filters=browseOnlineFrom.timestamp%20%3C%3D%201759833000%20AND%20browseOnlineTo.timestamp%20%3E%3D%201759833000%20AND%20categoryFilters%3Ajewelry_rings&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&maxValuesPerFacet=20&page=0"}]}'

# -------------------- Helper Functions --------------------
def safe_get(obj, path):
    """Safely get nested fields from dict/list using dot notation."""
    try:
        for key in path.split('.'):
            if isinstance(obj, list):
                obj = obj[int(key)]
            else:
                obj = obj.get(key)
        return obj if obj is not None else "N/A"
    except Exception:
        return "N/A"


def save_product_html(url, code):
    """Fetch and save product page HTML with retries."""
    folder = "tiffany_pages"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"{code}.html")

    # Skip if HTML already exists
    if os.path.exists(file_path):
        print(f"⏩ Skipping HTML (already exists): {file_path}")
        return

    for attempt in range(3):
        try:
            response = requests.get(url, headers=HEADERS, timeout=20)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(soup.prettify())
                print(f"🟢 Saved HTML ({attempt+1} try): {file_path}")
                return
            else:
                print(f"⚠️ Failed ({response.status_code}) for {code}, retrying...")
        except Exception as e:
            print(f"❌ HTML Save Error (try {attempt+1}) for {code}: {e}")
            time.sleep(3)
    print(f"⛔ Skipped HTML for {code} after 3 retries.")


# -------------------- Fetch and Process --------------------
print("🚀 Fetching up to 25 Tiffany products...")

response = requests.post(ALGOLIA_URL, headers=HEADERS, data=DATA)
print(f"🔗 Response Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    hits = data["results"][0]["hits"][:25]

    final_data = []
    new_products = 0

    for p in hits:
        style_id = str(safe_get(p, "styleId"))
        existing = collection.find_one({"styleId": style_id})

        if existing:
            print(f"⏩ Skipping {style_id} (already in MongoDB)")
            continue

        product_url = safe_get(p, "productUrl.canonicalUrl")
        if not product_url.startswith("http"):
            product_url = "https://www.tiffany.com" + product_url

        item = {
            "styleId": style_id,
            "availableQuantity": safe_get(p, "availableQuantity"),
            "isLowInventory": safe_get(p, "isLowInventory"),
            "_tags": safe_get(p, "_tags"),
            "itemMasterId": safe_get(p, "itemMasterId"),
            "level0Id": safe_get(p, "level0Id"),
            "categories": safe_get(p, "categories"),
            "motif": safe_get(p, "motif"),
            "productType": safe_get(p, "productType"),
            "family": safe_get(p, "family"),
            "legalCollection": safe_get(p, "legalCollection"),
            "hazardousMaterials": safe_get(p, "hazardousMaterials"),
            "merchindisingCollection": safe_get(p, "merchindisingCollection"),
            "materialSubType": safe_get(p, "materialSubType"),
            "primaryGemstoneSpecies": safe_get(p, "primaryGemstoneSpecies"),
            "bucketingMaterialSubType": safe_get(p, "bucketingMaterialSubType"),
            "designerAndCollectionFilter": safe_get(p, "designerAndCollectionFilter"),
            "primaryCategories": safe_get(p, "primaryCategories"),
            "collection": safe_get(p, "collection"),
            "brand": safe_get(p, "brand"),
            "maxOrderQuantity": safe_get(p, "maxOrderQuantity"),
            "designer": safe_get(p, "designer"),
            "color": safe_get(p, "color"),
            "baselineStrategy": safe_get(p, "baselineStrategy"),
            "size": safe_get(p, "size"),
            "urlImage": safe_get(p, "urlImage"),
            "images": safe_get(p, "images"),
            "description": safe_get(p, "description"),
            "additionalSpecifications": safe_get(p, "additionalSpecifications"),
            "manufacturerSkus": safe_get(p, "manufacturerSkus"),
            "videos": safe_get(p, "videos"),
            "productUrl": product_url,
            "parentPrice": safe_get(p, "parentPrice"),
            "variationsAvailable": safe_get(p, "variationsAvailable"),
            "relativeUrls": safe_get(p, "relativeUrls"),
        }

        final_data.append(item)
        new_products += 1

        save_product_html(product_url, style_id)
        time.sleep(random.uniform(1, 3))  # polite delay

    # -------------------- Store in MongoDB --------------------
    if final_data:
        collection.insert_many(final_data)
        print(f"\n✅ {new_products} new products inserted into MongoDB successfully!")

        # -------------------- Preview Data --------------------
        df = pd.DataFrame(final_data)
        print("\n🧾 Data Preview:")
        print(df.head())

        # Optional: Save to CSV
        df.to_csv("tiffany_products.csv", index=False)
        print("\n💾 Data saved to tiffany_products.csv")
    else:
        print("⚠️ No new products to insert.")
else:
    print("❌ API Request Failed. Check headers or URL.")
