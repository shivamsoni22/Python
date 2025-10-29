"""
Save as: scrape_counts_by_xpath.py
Usage:
    python scrape_counts_by_xpath.py
It will ask for mode (manual/auto). Default: manual.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, re, csv, datetime

# ---------- USER-PROVIDED XPATHs & URLs (from your message) ----------
XPATHS = {
    "Walmart": '//*[@id="results-container"]/div[1]/section/div/div/div/div/h2',
    "Target": '//*[@id="pageBodyContainer"]/div/div[1]/div/div/div[4]/div/div[3]/div/div/div/h2',
    "Albertsons": '//*[@id="search-summary_0"]/div/div/div/h1/span',
    "Publix": '//*[@id="main"]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/span',
    "Kroger": '//*[@id="content"]/div/div/div/div[2]/div[1]/div[2]/div',
    "Amazon": '//*[@id="search"]/span/div/h1/div/div[1]/div/h2/span[1]'
}

URLS = {
    "Walmart": "https://www.walmart.com/",
    "Target": "https://www.target.com/",
    "Albertsons": "https://www.albertsons.com/",
    "Publix": "https://www.publix.com/",
    "Kroger": "https://www.kroger.com/",
    "Amazon": "https://www.amazon.com/s?k=shampoo"
}

# ---------- helper functions ----------
def parse_count_from_text(text):
    if not text:
        return None
    t = text.replace('\xa0', ' ').strip()
    patterns = [
        r'of\s+over\s+([0-9,]+)\+?',          # "of over 30,000"
        r'of\s+([0-9,]+)\+?',                 # "of 30,000"
        r'([0-9,]+(?:,[0-9]{3})+)\+?\s*(?:results|items|Results|Items)',  # "30,000 results"
        r'([0-9,]+)\+?\s*(?:results|items|Results|Items)',              # "3000 results"
        r'([0-9,]+)\+' ,                      # "1,000+"
        r'([0-9,]{1,3}(?:,[0-9]{3})+)' ,      # any grouped number 1,234
        r'([0-9]+)'                           # fallback: any number
    ]
    for pat in patterns:
        m = re.search(pat, t, re.I)
        if m:
            return m.group(1)
    return None

def find_first_regex_count(page_source):
    # fallback on whole page text
    m = re.search(r'([0-9,]{1,})(?:\+)?\s*(?:results|items|Results|Items|results for)', page_source, re.I)
    if m:
        return m.group(1)
    m2 = re.search(r'of\s+([0-9,]{1,})(?:\+)?', page_source, re.I)
    if m2:
        return m2.group(1)
    return None

# ---------- setup browser ----------
mode = input("Choose mode (manual/auto) [manual]: ").strip().lower() or "manual"
headless_default = False if mode == "manual" else True

options = webdriver.ChromeOptions()
if headless_default:
    options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1400,1000")

print("[INFO] Starting Chrome driver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

results = []

try:
    print("[INFO] Browser started.")
    if mode == "manual":
        # open a neutral page so user can use same browser
        driver.get("https://www.google.com")
        print("\n[INSTRUCTION] Browser opened. Now switch to the browser window and manually navigate to each retailer, perform the SEARCH (e.g., type 'shampoo' and press Enter).")
        print("When you're on the results page and the count is visible, return here and press Enter to let the script read it.")
        print("Type 'skip' and Enter to skip a site without extracting.\n")

    # iterate sites
    for site in ["Walmart","Amazon","Target","Kroger","Publix","Albertsons"]:
        xpath = XPATHS.get(site)
        url = URLS.get(site)
        raw_text = None
        parsed = None
        status = "Not Found"
        timestamp = datetime.datetime.utcnow().isoformat()

        print("\n" + "="*40)
        print(f"[SITE] {site}")
        if mode == "auto":
            print(f"[AUTO] Opening {url} ...")
            driver.get(url)
            # allow some extra time, especially for dynamic JS
            time.sleep(6)
        else:
            print(f"[MANUAL] Please open the {site} search results page in the browser and make sure the count is visible.")
            print(f"Helpful URL (open in browser tab): {url}")
            cmd = input("When ready, press Enter to extract (or type 'skip' to skip): ").strip().lower()
            if cmd == "skip":
                status = "Skipped"
                print(f"[SKIP] Skipped {site}.")
                results.append({
                    "site": site, "raw_text": "", "parsed_count": "", "status": status, "timestamp": timestamp
                })
                continue
            # give a short pause to allow final JS render
            time.sleep(1)

        # Attempt 1: Try the exact XPath provided
        if xpath:
            try:
                print(f"[CHECK] Waiting for element by XPath: {xpath}")
                elem = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                raw_text = elem.text.strip()
                print(f"[FOUND] XPath text: {raw_text}")
                parsed = parse_count_from_text(raw_text)
                status = "OK (xpath)" if parsed else "Found (xpath,parse-failed)"
            except Exception as e:
                print(f"[WARN] XPath lookup failed: {e}")
                raw_text = None

        # Attempt 2: fallback - search for common classes or text on the page
        if not raw_text:
            try:
                page_source = driver.page_source
                # Quick regex on page_source
                candidate = find_first_regex_count(page_source)
                if candidate:
                    raw_text = candidate
                    parsed = parse_count_from_text(candidate) or candidate
                    status = "OK (regex-fallback)"
                    print(f"[FALLBACK] Regex found: {candidate}")
                else:
                    print("[FALLBACK] No regex count found on page source.")
            except Exception as e:
                print(f"[ERROR] Fallback regex failed: {e}")

        # Attempt 3: try searching visible texts that contain "results" or "items"
        if not raw_text:
            try:
                # broad XPath: any element with text() containing 'results' or 'items'
                broad_xpath = "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'results') or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'items')]"
                elements = driver.find_elements(By.XPATH, broad_xpath)
                print(f"[CHECK] Found {len(elements)} candidate elements with 'results'/'items' text.")
                for el in elements[:10]:
                    t = el.text.strip()
                    if not t:
                        continue
                    p = parse_count_from_text(t)
                    if p:
                        raw_text = t
                        parsed = p
                        status = "OK (broad-xpath)"
                        print(f"[FOUND] Broad match text: {t}")
                        break
            except Exception as e:
                print(f"[WARN] Broad xpath search error: {e}")

        # Final attempt: whole page plain text
        if not raw_text:
            try:
                page_txt = driver.find_element(By.TAG_NAME, 'body').text
                candidate = find_first_regex_count(page_txt)
                if candidate:
                    raw_text = candidate
                    parsed = parse_count_from_text(candidate) or candidate
                    status = "OK (page-text-fallback)"
                    print(f"[FALLBACK2] Page text candidate: {candidate}")
            except Exception as e:
                print(f"[WARN] Final page-text attempt failed: {e}")

        # If still nothing, leave Not Found
        if not raw_text:
            print(f"[RESULT] {site}: NOT FOUND. (Try increasing wait time, ensure the count is visible, or provide an updated XPath.)")
            status = "Not Found"

        # Normalize parsed: remove commas
        parsed_norm = ""
        if parsed:
            parsed_norm = parsed.replace(',', '').strip()

        results.append({
            "site": site,
            "raw_text": raw_text or "",
            "parsed_count": parsed_norm,
            "status": status,
            "timestamp": timestamp
        })
        print(f"[SAVED] {site} -> raw: '{raw_text}' | parsed: '{parsed_norm}' | status: {status}")

finally:
    # write CSV
    csv_file = "product_counts_shampoo.csv"
    try:
        with open(csv_file, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["site","raw_text","parsed_count","status","timestamp"])
            writer.writeheader()
            for r in results:
                writer.writerow(r)
        print(f"\n[INFO] Results saved to {csv_file}")
    except Exception as e:
        print(f"[ERROR] Could not write CSV: {e}")

    print("[INFO] Closing browser...")
    try:
        driver.quit()
    except:
        pass

    print("[DONE] Script finished.")
