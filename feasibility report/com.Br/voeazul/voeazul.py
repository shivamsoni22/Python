import requests
import urllib.parse

# -----------------------------
# Headers & Cookies (browser mimic)
# -----------------------------
cookies = {
    'AZAB': 'A',
    'bm_ss': 'ab8e18ef4e',
    'AMCVS_04EA1613539237590A490D4D%40AdobeOrg': '1',
    # ... baki cookies yaha add karein ...
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
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
# Target URL with params
# -----------------------------
base_url = "https://www.voeazul.com.br/us/en/home/selecao-voo"
params = {
    'c[0].ds': 'ORY',
    'c[0].std': '10/05/2025',
    'c[0].as': 'VCP',
}

query_string = urllib.parse.urlencode(params, safe=":/")
target_url = f"{base_url}?{query_string}"

# -----------------------------
# Send direct request
# -----------------------------
try:
    response = requests.get(target_url, headers=headers, cookies=cookies, timeout=30)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Response Preview:\n", response.text[:1000])  # pehle 1000 characters
    else:
        print("Error Response:\n", response.text)
except Exception as e:
    print("⚠️ Error:", e)
