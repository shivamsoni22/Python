import requests
import urllib.parse

# 🔑 Scrape.do token (apna actual token yaha daalo)
SCRAPEDO_TOKEN = "f42a5b59aec3467e97a8794c611c436b91589634343"

# -----------------------------
# Headers & Cookies (browser mimic)
# -----------------------------
cookies = {
    'prediggoSession': 'f64bee56-83c1-42bf-b99a-69c78d912ded',
    'PHPSESSID': 'b1fb6bb372ec71ad771de98baa6ca9a7',
    'OptanonAlertBoxClosed': '2025-09-12T08:46:38.703Z',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Sep+12+2025+14%3A16%3A38+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0f130f67-84d7-4dac-b7ef-bf738b470ccf&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CBG357%3A1',
    'predcwwk': '36c4ec2e-5729-4804-b46a-103fcd92d544',
    '_ga': 'GA1.1.703501457.1757666806',
    '_ga_510QFBS2GX': 'GS2.1.s1757666806$o1$g0$t1757666806$j60$l0$h93787950',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
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
# Target URL (Denner product with variant)
# -----------------------------
base_url = "https://www.denner.ch/fr/actions-et-assortiment/huile-vegetale-sabo~p029043"
variant_id = "781c076a-19d5-4282-9613-ef3fa10a5914"

# Build original product URL
target_url = f"{base_url}?variant={variant_id}"
encoded_url = urllib.parse.quote(target_url)

# Scrape.do API URL
scrape_url = f"http://api.scrape.do/?token={SCRAPEDO_TOKEN}&url={encoded_url}"

# -----------------------------
# Send request via Scrape.do
# -----------------------------
try:
    response = requests.get(scrape_url, headers=headers, cookies=cookies, timeout=30)
    print("Status Code:", response.status_code)
    print("response headers:", response.headers)
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
