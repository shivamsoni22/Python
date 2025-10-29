# import json
# import requests
# from pymongo import MongoClient
# from lxml import html
# import time
#
# # --- MongoDB Connection ---
# client = MongoClient("mongodb://localhost:27017/")
# db = client["thehouseofrare1234_db"]
# collection = db["products"]
#
# # --- API Headers ---
# headers_api = {
#     'accept': '*/*',
#     'origin': 'https://thehouseofrare.com',
#     'referer': 'https://thehouseofrare.com/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
# }
#
# # --- API Base URL ---
# base_url = "https://search.unbxd.io/e94cac92f0f2da84ae5ca93f42a57658/ss-unbxd-aapac-prod-shopify-houseofrare58591725608684/search"
#
# # --- Function to scrape product page ---
# def scrape_product_page(product_url):
#     data = {
#         "title_page": "N/A",
#         "sub_title_page": "N/A",
#         "mrp_page": "N/A",
#         "selling_price_page": "N/A",
#         "discount_par_page": "N/A",
#         "description": "N/A",
#     }
#     try:
#         res = requests.get("https://thehouseofrare.com" + product_url, headers=headers_api, timeout=15)
#         if res.status_code == 200:
#             tree_html = html.fromstring(res.text)
#
#             title_h1 = tree_html.xpath('//h1[@class="main-title"]//span//text()')
#             title_h2 = tree_html.xpath('//h2[@class="sub-title"]/text()')
#             mrp = tree_html.xpath('//span[@class="money"]/text()')
#             selling_price = tree_html.xpath('//span[@class="regular-price"]/span//text()')
#             discount_par = tree_html.xpath('//span[@class="perc_price"]//text()')
#             description = tree_html.xpath('//div[@class="content-wrapper"]//p//text()')
#
#             data.update({
#                 "title_page": title_h1[0] if title_h1 else "N/A",
#                 "sub_title_page": title_h2[0] if title_h2 else "N/A",
#                 "mrp_page": mrp[0] if mrp else "N/A",
#                 "selling_price_page": selling_price[0] if selling_price else "N/A",
#                 "discount_par_page": discount_par[0] if discount_par else "N/A",
#                 "description": " ".join(description).strip() if description else "N/A",
#             })
#     except Exception as e:
#         print("⚠️ Scraping error:", e)
#
#     return data
#
#
# # --- Pagination Loop ---
# rows = 20
# start = 0
# page = 1
#
# while True:
#     print(f"\n📄 Fetching Page {page} (start={start})...")
#
#     params = {
#         'q': 'shirt',
#         'uid': 'uid-1759241957082-60561',
#         'variants': 'true',
#         'variants.fields': 'variantId,v_Size,v_availableForSale,v_sku',
#         'variants.count': '20',
#         'fields': 'title,uniqueId,price,imageUrl,productUrl,meta_my_fields_main_title,handle,images,variants,meta_my_fields_sub_title,compareAtPrice,computed_discount,grouped_products,meta_custom_variant_color_image,meta_my_fields_COLOR,swatch_image_url,meta_custom_gender,meta_custom_best_price,best_price',
#         'filter': 'meta_custom_gender_uFilter:"MEN"',
#         'start': str(start),
#         'rows': str(rows),
#     }
#
#     response = requests.get(base_url, params=params, headers=headers_api)
#     tree = json.loads(response.text)
#
#     if "response" not in tree or "products" not in tree["response"]:
#         print("⚠️ No products found, stopping pagination.")
#         break
#
#     products = tree["response"]["products"]
#     if not products:
#         print("✅ All pages fetched. Stopping.")
#         break
#
#     print(f"🔹 Products found: {len(products)}")
#
#     # --- Loop products ---
#     for product in products:
#         product_url = product.get('productUrl', "N/A")
#
#         doc = {
#             "title": product.get('title', "N/A"),
#             "main_title": product.get('meta_my_fields_main_title', "N/A"),
#             "sub_title": product.get('meta_my_fields_sub_title', "N/A"),
#             "price": product.get('price', "N/A"),
#             "compareAtPrice": product.get('compareAtPrice', "N/A"),
#             "best_price": product.get('best_price', "N/A"),
#             "discount": product.get('computed_discount', "N/A"),
#             "productUrl": product_url,
#             "handle": product.get('handle', "N/A"),
#             "color": product.get('meta_my_fields_COLOR', "N/A"),
#             "gender": product.get('meta_custom_gender', "N/A"),
#             "imageUrl": product.get('imageUrl', "N/A"),
#             "images": product.get('images', []),
#             "variants": product.get('variants', []),
#         }
#
#         # Scrape detail page
#         if product_url != "N/A":
#             scraped_data = scrape_product_page(product_url)
#             doc.update(scraped_data)
#
#         # Save to MongoDB
#         collection.update_one({"productUrl": doc["productUrl"]}, {"$set": doc}, upsert=True)
#         print(f"✅ Saved: {doc['title']}")
#
#     # Pagination step
#     start += rows
#     page += 1
#     time.sleep(2)  # avoid server overload
#
# print("\n🎉 All products from all pages saved to MongoDB successfully!")



import json
import requests
from pymongo import MongoClient
from lxml import html

# --- MongoDB Connection ---
client = MongoClient("mongodb://localhost:27017/")
db = client["thehouseofrare_db"]
products_collection = db["products"]
pages_collection = db["pages"]

# --- API Headers ---
headers_api = {
    'accept': '*/*',
    'origin': 'https://thehouseofrare.com',
    'referer': 'https://thehouseofrare.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

# --- API Base URL ---
base_url = "https://search.unbxd.io/e94cac92f0f2da84ae5ca93f42a57658/ss-unbxd-aapac-prod-shopify-houseofrare58591725608684/search"


# --- Function to scrape product detail page ---
def scrape_product_page(product_url):
    data = {
        "title_page": "N/A",
        "sub_title_page": "N/A",
        "mrp_page": "N/A",
        "selling_price_page": "N/A",
        "discount_par_page": "N/A",
        "description": "N/A",
    }
    try:
        res = requests.get("https://thehouseofrare.com" + product_url, headers=headers_api, timeout=15)
        if res.status_code == 200:
            tree_html = html.fromstring(res.text)

            title_h1 = tree_html.xpath('//h1[@class="main-title"]//span//text()')
            title_h2 = tree_html.xpath('//h2[@class="sub-title"]/text()')
            mrp = tree_html.xpath('//span[@class="money"]/text()')
            selling_price = tree_html.xpath('//span[@class="regular-price"]/span//text()')
            discount_par = tree_html.xpath('//span[@class="perc_price"]//text()')
            description = tree_html.xpath('//div[@class="content-wrapper"]//p//text()')

            data.update({
                "title_page": title_h1[0] if title_h1 else "N/A",
                "sub_title_page": title_h2[0] if title_h2 else "N/A",
                "mrp_page": mrp[0] if mrp else "N/A",
                "selling_price_page": selling_price[0] if selling_price else "N/A",
                "discount_par_page": discount_par[0] if discount_par else "N/A",
                "description": " ".join(description).strip() if description else "N/A",
            })
    except Exception as e:
        print("⚠️ Scraping error:", e)

    return data


# --- Page Config ---
rows = 20
start = 0
page_number = 1

# --- Check if this page is already scraped ---
page_doc = pages_collection.find_one({"page_number": page_number, "rows": rows, "start": start})

if page_doc and page_doc.get("is_scraped"):
    print(f"✅ Page {page_number} already scraped earlier. Fetching from DB only...")
    for product in products_collection.find({"page_number": page_number}):
        print("🔹", product["title"])
else:
    print(f"\n📄 Fetching Page {page_number} (start={start})...")

    params = {
        'q': 'shirt',
        'uid': 'uid-1759241957082-60561',
        'variants': 'true',
        'variants.fields': 'variantId,v_Size,v_availableForSale,v_sku',
        'variants.count': '20',
        'fields': 'title,uniqueId,price,imageUrl,productUrl,meta_my_fields_main_title,handle,images,variants,meta_my_fields_sub_title,compareAtPrice,computed_discount,grouped_products,meta_custom_variant_color_image,meta_my_fields_COLOR,swatch_image_url,meta_custom_gender,meta_custom_best_price,best_price',
        'filter': 'meta_custom_gender_uFilter:"MEN"',
        'start': str(start),
        'rows': str(rows),
    }

    response = requests.get(base_url, params=params, headers=headers_api)
    tree = json.loads(response.text)

    if "response" in tree and "products" in tree["response"]:
        products = tree["response"]["products"]
        print(f"🔹 Products found: {len(products)}")

        for product in products:
            product_url = product.get('productUrl', "N/A")

            doc = {
                "page_number": page_number,
                "start": start,
                "rows": rows,
                "title": product.get('title', "N/A"),
                "main_title": product.get('meta_my_fields_main_title', "N/A"),
                "sub_title": product.get('meta_my_fields_sub_title', "N/A"),
                "price": product.get('price', "N/A"),
                "compareAtPrice": product.get('compareAtPrice', "N/A"),
                "best_price": product.get('best_price', "N/A"),
                "discount": product.get('computed_discount', "N/A"),
                "productUrl": product_url,
                "handle": product.get('handle', "N/A"),
                "color": product.get('meta_my_fields_COLOR', "N/A"),
                "gender": product.get('meta_custom_gender', "N/A"),
                "imageUrl": product.get('imageUrl', "N/A"),
                "images": product.get('images', []),
                "variants": product.get('variants', []),
            }

            # Scrape product detail page
            if product_url != "N/A":
                scraped_data = scrape_product_page(product_url)
                doc.update(scraped_data)

            # Save to MongoDB
            products_collection.update_one({"productUrl": doc["productUrl"]}, {"$set": doc}, upsert=True)
            print(f"✅ Saved: {doc['title']}")

        # Mark page as scraped
        pages_collection.update_one(
            {"page_number": page_number, "rows": rows, "start": start},
            {"$set": {"is_scraped": True}},
            upsert=True
        )
        print(f"📌 Page {page_number} marked as scraped.")
    else:
        print("⚠️ No products found in API response.")
