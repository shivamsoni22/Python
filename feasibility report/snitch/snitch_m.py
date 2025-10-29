# import json
#
# import requests
# from lxml import html
# from lxml.html import fromstring
#
# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Headers': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Origin': 'https://www.snitch.com',
#     'Referer': 'https://www.snitch.com/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
#     'client-id': 'snitch_secret',
#     'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# params = {
#     'page': '1',
#     'limit': '100',
#     'keyword': 'jins',
# }
#
# response = requests.get('https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/search', params=params, headers=headers)
#
#
#
# tree = json.loads(response.text)
#
# main_product = tree['data']['products']
# print(len(main_product))
# for product in main_product:
#     title = product['title']
#     color = data.products[0].color
#     selling_price =
#     price
#     average_rating = data.products[0].average_rating
#     img = data.products[0].images
#     mrp = data.products[0].mrp
#     selling_price = data.products[0].selling_price
#
#     selling_price = data.products[0].short_description
#     total_ratings_count = data.products[0].total_ratings_count
#     total_rewiews_count = data.products[0].total_rewiews_count
#     variants = data.products[0].variants



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

main_product = tree['data']['products']
print("Total products:", len(main_product))

# --- Save to MongoDB ---
for product in main_product:
    doc = {
        "title": product.get('title'),
        "color": product.get('color'),
        "selling_price": product.get('selling_price'),
        "mrp": product.get('mrp'),
        "average_rating": product.get('average_rating'),
        "total_ratings_count": product.get('total_ratings_count'),
        "total_reviews_count": product.get('total_reviews_count'),
        "short_description": product.get('short_description'),
        "images": product.get('images', []),
        "variants": product.get('variants', []),
        "product_url": product.get('url') or f"https: // www.snitch.com / products / {product.get('handle')}"
    }

    # Agar duplicate title na aaye to update_one + upsert use karenge
    collection.update_one({"title": doc["title"]}, {"$set": doc}, upsert=True)

print("✅ Products saved to MongoDB successfully!")


