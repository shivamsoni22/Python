# "brand" = //a[@id="bylineInfo"]//text()
#  = //*[@id="wayfinding-breadcrumbs_feature_div"]//ul//li//span/a/text()
# product name =//span[@id="productTitle"]/text()
# price =//*[@id="corePriceDisplay_desktop_feature_div"]//span[@class="a-price-whole"]/text()
# mrp =//span[@class="a-size-small aok-offscreen"]/text()
# stock= //*[@id="availability"]/span/text()
# about = //*[@id="productFactsDesktopExpander"]//div/h3//ul//li//span/text()


import requests

cookies = {
    'csm-sid': '766-9203016-7131952',
    'session-id': '523-4238945-6227465',
    'i18n-prefs': 'INR',
    'lc-acbin': 'en_IN',
    'ubid-acbin': '262-8411454-0837854',
    'x-amz-captcha-1': '1758022515583655',
    'x-amz-captcha-2': 'qbr6mDUL8bN28E0SF0wB9A==',
    'session-token': 'Y8LZ0oimnGWcGINFbOZ1FBEPxCVdvrEOnC/QYfwfwD1hUMwtZ3s6r8rmmmI7vdrVRIQBZGDn6XmqRHTN6wveZXInhdT27+jhHSw9weR/5ElJZZPgqJJwVNf5VnQ1GdxNtcgXNtkmEXQcorIGZa+qwOR7jrAhDH12LL2tQOGiQ5HE6rb8IXlwSUlIFii6qwqynF8DFbMwINovlKPzjKs6XGUsRg4YPQAfBjAvj7XvhW8wv0K3dAzk8fy1mxaOZwbTgUVf+ndFpQ+uW1AUG+pujdAQiI292tME9AeU8WSQnWUp7X103m1Ux6euWyO69nNn5GZAc+2QpsWqenb9HK9VnFEyVdvg/GC/',
    'session-id-time': '2082787201l',
    'csm-hit': 'tb:B0NDYE84FB5YP57Q3G88+s-2WZ2Z3B0TSB9W1V4B6BH|1758016961527&t:1758016961532&adb:adblk_no',
    'rxc': 'AAE81UgMROqESuz9LPg',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1.5',
    'ect': '4g',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/errors/validateCaptcha?amzn=DKOfJDfMohmghmZVrZr5bA%3D%3D&amzn-r=%2Fdp%2FB0CHMRPRRQ%3Fref%3Dcm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM%26ref_%3Dcm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM%26social_share%3Dcm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM&field-keywords=HFXYRA',
    'rtt': '150',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.5',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-ch-viewport-width': '1280',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'viewport-width': '1280',
    # 'cookie': 'csm-sid=766-9203016-7131952; session-id=523-4238945-6227465; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=262-8411454-0837854; x-amz-captcha-1=1758022515583655; x-amz-captcha-2=qbr6mDUL8bN28E0SF0wB9A==; session-token=Y8LZ0oimnGWcGINFbOZ1FBEPxCVdvrEOnC/QYfwfwD1hUMwtZ3s6r8rmmmI7vdrVRIQBZGDn6XmqRHTN6wveZXInhdT27+jhHSw9weR/5ElJZZPgqJJwVNf5VnQ1GdxNtcgXNtkmEXQcorIGZa+qwOR7jrAhDH12LL2tQOGiQ5HE6rb8IXlwSUlIFii6qwqynF8DFbMwINovlKPzjKs6XGUsRg4YPQAfBjAvj7XvhW8wv0K3dAzk8fy1mxaOZwbTgUVf+ndFpQ+uW1AUG+pujdAQiI292tME9AeU8WSQnWUp7X103m1Ux6euWyO69nNn5GZAc+2QpsWqenb9HK9VnFEyVdvg/GC/; session-id-time=2082787201l; csm-hit=tb:B0NDYE84FB5YP57Q3G88+s-2WZ2Z3B0TSB9W1V4B6BH|1758016961527&t:1758016961532&adb:adblk_no; rxc=AAE81UgMROqESuz9LPg',
}

params = {
    'ref': 'cm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM',
    'ref_': 'cm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM',
    'social_share': 'cm_sw_r_cso_cp_apan_dp_4WGBKRCSPY9NRAX86KNM',
    'th': '1',
}

response = requests.get('https://www.amazon.in/dp/B0CHMRPRRQ', params=params, cookies=cookies, headers=headers)