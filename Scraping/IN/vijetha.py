import os
import requests
import json
from pymongo import MongoClient


def get_data():
    page_number = 1
    items = []

    # ✅ MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")  # change if needed
    db = client["vijetha"]       # database name
    collection = db["Tea_products"]  # collection name

    while True:
        file_name = f'tea_{page_number}.html'

        # If file already exists, read from it
        if os.path.exists(file_name):
            print(f"📂 Reading saved file: {file_name}")
            with open(file_name, 'r', encoding='utf-8') as f:
                response_text = f.read()
            try:
                json_data = json.loads(response_text)
            except Exception as e:
                print(f"❌ Error parsing saved file {file_name}: {e}")
                break
        else:
            # Make request if file not found
            print(f"🌐 Fetching page {page_number} from API...")
            cookies = {
                '_fbp': 'fb.1.1752135538647.311022885933954599',
                'theme': 'Moonshot',
            }

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en',
                'referer': f'https://vijetha.in/search?q=tea',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/139.0.0.0 Safari/537.36',
            }

            params = {
                'layoutType': 'GRID',
                'loadMoreType': 'INFINITE',
                'page': str(page_number),
                'q': 'tea',
                'storeId': '24400',
            }

            try:
                response = requests.get(
                    'https://vijetha.in/api/product',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    timeout=15
                )
                response.raise_for_status()
                response_text = response.text
                json_data = response.json()

                # Save page locally
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(response_text)
                print(f"💾 Saved: {file_name}")

            except Exception as e:
                print(f"❌ Error on page {page_number}: {e}")
                break

        # ✅ Check if "data" is missing or None
        data = json_data.get("data")
        if not data or not isinstance(data, dict) or not data.get("product"):
            print(f"✅ No more products found on page {page_number}. Stopping.")
            break

        # Collect product info
        for product in data.get("product", []):
            variant = product['variants'][0] if product.get("variants") else {}
            store_data = variant.get('storeSpecificData', [{}])[0]

            # ✅ Convert mrp and discount to float
            mrp_raw = store_data.get("mrp")
            discount_raw = store_data.get("discount")

            try:
                mrp = float(mrp_raw) if mrp_raw is not None else None
            except:
                mrp = None

            try:
                discount = float(discount_raw) if discount_raw is not None else None
            except:
                discount = None

            # ✅ Price calculation
            if mrp is not None and discount is not None:
                price = mrp - discount
                discount_percent = round((discount / mrp) * 100, 2)
            elif mrp is not None:
                price = mrp
                discount_percent = 0
            else:
                price = None
                discount_percent = None

            # ✅ Brand info safe handling
            brand = product.get("brand") or {}
            brand_info = {
                "id": brand.get("id", "N/A"),
                "image": brand.get("image", "N/A"),
                "logo": brand.get("logo", "N/A"),
                "name": brand.get("name", "N/A"),
                "productsCount": brand.get("productsCount", "N/A"),
                "slug": brand.get("slug", "N/A")
            }

            # ✅ Mandatory fields safe handling
            product_id = product.get("id", "N/A")
            product_name = variant.get("fullName", "N/A")
            product_url = f"https://vijetha.in/product/{product.get('slug')}" if product.get("slug") else "N/A"

            # ✅ Images
            images = variant.get("images") or ["N/A"]
            images_extra = variant.get("imagesExtra") or ["N/A"]

            item = {
                "id": product_id,
                "name": product_name,
                "url": product_url,
                "mrp": mrp,
                "discount_value": discount,
                "discount_percent": discount_percent,
                "price": price,
                "slug": product.get("slug", "N/A"),
                "stock": store_data.get("stock") if store_data.get("stock") is not None else "N/A",
                "storeId": store_data.get("storeId") if store_data.get("storeId") is not None else "N/A",
                "tax": store_data.get("tax") if store_data.get("tax") else "N/A",
                "unit": store_data.get("unit") if store_data.get("unit") is not None else "N/A",
                "unlimitedStock": store_data.get("unlimitedStock") if store_data.get("unlimitedStock") is not None else "N/A",
                "averageRating": product.get("averageRating", "N/A"),
                "brand": brand_info,
                "clientItemId": product.get("clientItemId", "N/A"),
                "createdAt": product.get("createdAt", "N/A"),
                "description": product.get("description", "N/A"),
                "offers": product.get("offers", "N/A"),
                "images": images,
                "imagesExtra": images_extra
            }

            items.append(item)
            print('item--->', item)

            # ✅ Insert into MongoDB (ignore duplicates by slug)
            if item.get("slug") and item.get("slug") != "N/A":
                collection.update_one(
                    {"slug": item["slug"]},
                    {"$set": item},
                    upsert=True
                )

        page_number += 1

    return items


if __name__ == '__main__':
    products = get_data()
    print(f"\n📦 Total products collected: {len(products)}")
