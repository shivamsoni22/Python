import requests
import urllib.parse

# 🔑 Scrape.do token (apna actual token yaha daalo)
# SCRAPEDO_TOKEN = "f42a5b59aec3467e97a8794c611c436b91589634343"

# -----------------------------
# Headers & Cookies (browser mimic)
# -----------------------------
cookies = {
    '_pk_id.4.fcd7': '9c76ae3dd8264bcb.1757665569.',
    '_pk_ses.4.fcd7': '1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.leslibraires.fr/recherche/?q=https%3A%2F%2Fwww.leslibraires.fr%2Flivre%2F24540273-le-corbeau-qui-maimait-abdelaziz-baraka-sakin-zulma',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
}

# -----------------------------
# Target URL (leslibraires product)
# -----------------------------
target_url = "https://www.leslibraires.fr/livre/24540273-le-corbeau-qui-maimait-abdelaziz-baraka-sakin-zulma"
encoded_url = urllib.parse.quote(target_url)

# Scrape.do API URL
scrape_url = f"http://api.scrape.do/?token={SCRAPEDO_TOKEN}&url={encoded_url}"

# -----------------------------
# Send request via Scrape.do
# -----------------------------
try:
    response = requests.get(scrape_url, headers=headers, cookies=cookies, timeout=30)
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    # print("Response Preview:\n", response.text[:500])  # sirf pehle 500 chars
except Exception as e:
    print("⚠️ Error:", e)

# -----------------------------
# (Optional) Simple Test with httpbin
# -----------------------------
try:
    test_url = urllib.parse.quote("https://httpbin.org/anything")
    test_scrape = f"http://api.scrape.do/?token={SCRAPEDO_TOKEN}&url={test_url}"

    test_response = requests.get(test_scrape, timeout=30)
    print("\n✅ Test Request Response:")
    print(test_response.text)
except Exception as e:
    print("⚠️ Test Error:", e)
