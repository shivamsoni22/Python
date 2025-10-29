import json
import requests
from pymongo import MongoClient

# --- MongoDB Connection ---
client = MongoClient("mongodb://localhost:27017/")  # apna Mongo URL daal do
db = client["snitch_db"]  # database name
collection = db["products"]  # collection name

# --- API Call ---
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Headers': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.snitch.com',
    'Referer': 'https://www.snitch.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'client-id': 'snitch_secret',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'page': '1',
    'limit': '100',
    'keyword': 'jins',
}

response = requests.get(
    'https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/search',
    params=params,
    headers=headers
)

tree = json.loads(response.text)

main_products = tree['data']['products']
print("Total products:", len(main_products))

# --- Save to MongoDB ---
for product in main_products:
    doc = {
        "title": product.get("title", "N/A"),
        "short_description": product.get("short_description", "N/A"),
        "product_url": product.get("url") or f"https://www.snitch.com/products/{product.get('handle', '')}",

        # Pricing
        "selling_price": product.get("selling_price", "N/A"),
        "mrp": product.get("mrp", "N/A"),

        # Ratings
        "average_rating": product.get("average_rating", "N/A"),
        "total_ratings_count": product.get("total_ratings_count", "N/A"),
        "total_reviews_count": product.get("total_rewiews_count", "N/A"),

        # Product Attributes
        "color": product.get("color", "N/A"),
        "fit": product.get("fit", "N/A"),
        "material": product.get("material", "N/A"),
        "pattern": product.get("pattern", "N/A"),
        "sleeves": product.get("sleeves", "N/A"),
        "occassion": product.get("occassion", "N/A"),
        "shopify_product_type": product.get("shopify_product_type", "N/A"),

        # Images
        "preview_image": product.get("preview_image", "N/A"),
        "images": product.get("images", []),

        # Model Info
        "model_info": product.get("model_info", "N/A"),

        # Variants
        "variants": product.get("variants", []),
        "color_variants_count": product.get("color_variants_count", "N/A"),
        "color_variants_ids": product.get("color_variants_ids", []),
        "colors": product.get("colors", []),

        # Extra
        "handle": product.get("handle", "N/A"),
        "washcare": product.get("washcare", "N/A"),
    }

    # Upsert to avoid duplicates
    collection.update_one({"title": doc["title"]}, {"$set": doc}, upsert=True)

print("✅ Products with clean fields saved to MongoDB successfully!")
