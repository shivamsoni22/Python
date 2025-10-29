import requests
import urllib.parse

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

base_url = "https://www.voeazul.com.br/us/en/home/selecao-voo"
params = {
    "c[0].ds": "CGH",   # Origin
    "c[0].std": "10/10/2025",  # Date
    "c[0].as": "FLN",   # Destination
}

query_string = urllib.parse.urlencode(params, safe=":/")
target_url = f"{base_url}?{query_string}"

try:
    response = requests.get(target_url, headers=headers, timeout=30)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Response Preview:\n", response.text[:1000])
        print("Error Response:\n", response.headers)
    else:
        print("Error Response:\n", response.text)

except Exception as e:
    print("⚠️ Error:", e)
