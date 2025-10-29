import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from urllib3.contrib.emscripten.fetch import send_jspi_request

# Cookies (may or may not be required)
cookies = {
    '_fbp': 'fb.1.1752135538647.311022885933954599',
    'theme': 'Moonshot',
}

# Headers (to mimic browser)
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en',
    'priority': 'u=1, i',
    'referer': 'https://vijetha.in/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}


# Function to fetch a single product
def fetch_product(product_slug):
    params = {
        'url': product_slug,
        'storeId': '24400',
        'orderType': 'DELIVERY',
    }

    try:
        response = requests.get(
            'https://vijetha.in/api/layout/product',
            params=params,
            cookies=cookies,
            headers=headers,
            timeout=30
        )
        if response.status_code == 200:
            return {product_slug: response.json()}
        else:
            return {product_slug: f"❌ Failed (status {response.status_code})"}
    except Exception as e:
        return {product_slug: f"⚠️ Error: {e}"}


# Example product slugs
products = [
    "agni-leaf-tea-powder-refill-4",
    "red-label-tea-1kg",
    "tata-salt-1kg",
    "fortune-oil-5l",
    "aashirvaad-atta-10kg",
    "bru-instant-coffee-200g",
    "sundrop-refined-oil-1l",
    "good-day-cashew-cookies-600g",
    "colgate-paste-200g",
    "detergent-powder-1kg",
]

# Run with ThreadPool (10 workers)
results = []
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_slug = {executor.submit(fetch_product, slug): slug for slug in products}

    for future in as_completed(future_to_slug):
        results.append(future.result())

print("Final Results:")
for r in results:
    print(r)




