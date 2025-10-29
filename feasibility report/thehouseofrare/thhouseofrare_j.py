import json
import requests
from pymongo import MongoClient

# --- MongoDB Connection ---
client = MongoClient("mongodb://localhost:27017/")  # Apna Mongo URL daal do
db = client["thehouseofrare_db"]  # database name
collection = db["products"]  # collection name

# --- API Headers ---
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://thehouseofrare.com',
    'priority': 'u=1, i',
    'referer': 'https://thehouseofrare.com/',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'unbxd-device-type': '{ "type":"desktop" , "os": "Windows" , "source": "browser" }',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

# --- API Params ---
params = {
    'q': 'shirt',
    'uid': 'uid-1759241957082-60561',
    'variants': 'true',
    'variants.fields': 'variantId,v_Size,v_availableForSale,v_sku',
    'variants.count': '20',
    'fields': 'title,uniqueId,price,imageUrl,productUrl,meta_my_fields_main_title,handle,images,variants,meta_my_fields_sub_title,compareAtPrice,computed_discount,grouped_products,meta_custom_variant_color_image,meta_my_fields_COLOR,swatch_image_url,meta_custom_gender,meta_custom_best_price,best_price',
    'spellcheck': 'true',
    'filter': 'meta_custom_gender_uFilter:"MEN"',
    'start': '0',
    'rows': '20',
}

# --- API Request ---
response = requests.get(
    'https://search.unbxd.io/e94cac92f0f2da84ae5ca93f42a57658/ss-unbxd-aapac-prod-shopify-houseofrare58591725608684/search',
    params=params,
    headers=headers,
)

tree = json.loads(response.text)

main_product = tree['response']['products']  # ✅ sahi path
print("Total products:", len(main_product))

# --- Save to MongoDB ---
for product in main_product:
    doc = {
        "title": product.get('title'),
        "main_title": product.get('meta_my_fields_main_title'),
        "sub_title": product.get('meta_my_fields_sub_title'),
        "price": product.get('price'),
        "compareAtPrice": product.get('compareAtPrice'),
        "best_price": product.get('best_price'),
        "productUrl": product.get('productUrl'),
        "score": product.get('score'),
        "color": product.get('meta_my_fields_COLOR'),
        "imageUrl": product.get('imageUrl'),
        "images": product.get('images', []),
        "variants": product.get('variants', []),
    }

    # Duplicate avoid karne ke liye upsert
    collection.update_one({"productUrl": doc["productUrl"]}, {"$set": doc}, upsert=True)

print("✅ Products saved to MongoDB successfully!")
