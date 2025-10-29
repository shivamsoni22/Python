import requests

cookies = {
    'localization': 'IN',
    '_shopify_y': '36ada731-e9a9-49eb-adb1-7eef06e9e458',
    '_tracking_consent': '3.AMPS_USNJ_f_f_sTSThbj5RcSvyhp3l2-NfA',
    '_orig_referrer': '',
    '_landing_page': '%2F',
    'fastrr_uuid': 'cfffde98-a36c-4d79-a363-8c580058a968',
    'fastrr_usid': 'cfffde98-a36c-4d79-a363-8c580058a968-1759241951857',
    'fastrrPrefetchTriggered': '1',
    '_gcl_au': '1.1.1420475226.1759241952',
    '__spdt': 'c7b5d01aa4e74aa8b67208b821edc438',
    'fastrrUserIdEventTriggered': '1',
    'cl49824bjrqa63_uid': 'cl49824bjrqa63d3d434a7-1966-4ae4-b065-b39ea3e35bc7',
    'cl49824bjrqa63_utmParams': '%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3A%22Direct%22%7D',
    'cl49824bjrqa63_gid': 'cl49824bjrqa63c0714956-d3fb-4ab2-a26f-e0dd1618ef33',
    'KP_MERCHANT_CONFIG': '{"id":131,"merchantId":"19g6ilvf14ycs","name":"Rare rabbit Kwikpass","host":"rarerabbit.myshopify.com","platform":"Shopify","kwikpassEnabled":true,"isWhatsappOtpLessActive":true,"isTruecallerActive":true,"integrationType":"PLUGIN","isLogoutBtnDisabled":false,"popupBreakpoint":"1240px","apiKey":"66c7fb48f170a338f38b7c795b1db597","isPublicAppInstalled":false,"customerIntelligenceEnabled":false,"customerIntelligenceMetrics":null,"marketingPopupGlobalLimit":"1","customerAccountsVersion":"classic","kpAppName":null,"isCustomAccountPageEnabled":false,"isPagePingEnabled":false,"pagePingConfig":null,"thirdPartyServiceProviders":[],"kpRequestId":"faaef8fd-9f6e-447d-be86-f20dd8cfb3e4"}',
    'FP_CONTROLS_DATA': '{"fpFlowAllowd":false,"vIdGeneration":{"enabled":false,"limitReached":true},"apiConfigurations":{},"generator":""}',
    '_ka_c_ce': '%5B%5D',
    '_ka_c': '%7B%22isConfigured%22%3Afalse%2C%22standardEvents%22%3A%5B%5D%7D',
    'shopify_api_tags': '["KWIKPASS"]',
    'shopify_api_tags_login_modal': '["KWIKPASS"]',
    'unbxd.userId': 'uid-1759241957082-60561',
    'unbxd.visit': 'first_time',
    'unbxd.visitId': 'visitId-1759241957090-62095',
    'kp_session_id': '5ac9810f-488f-4d92-b415-1ff4b67ea4e1',
    'kp_user_id': '01999afd-f31d-707d-96c3-8988e6a94a86',
    '_sp_ses.d9c8': '*',
    'SP_DUID': 'd05099ef-f984-4344-9f3c-c3ff1b984cbe',
    '_scid': '4Ww-YBLtFbGkrdGRJbiNWOpx-uG5GFBI',
    'afUserId': '51807e91-99b3-4d20-8f69-0d0e30071649-p',
    'AF_SYNC': '1759241960336',
    '_ScCbts': '%5B%5D',
    '_clck': '1yoi1pm%5E2%5Efzr%5E1%5E2099',
    '_gid': 'GA1.2.1009669663.1759241966',
    '_gat_gtag_UA_63311952_3': '1',
    '_gat_UA-63311952-1': '1',
    '_fbp': 'fb.1.1759241969916.301323445438827611',
    'cl49824bjrqa63_eids': '%7B%22eids%22%3A%7B%22_shopify_y%22%3A%2236ada731-e9a9-49eb-adb1-7eef06e9e458%22%7D%2C%22eidsTracked%22%3Atrue%7D',
    '_sctr': '1%7C1759170600000',
    'imageAnimation': 'true',
    'moe_uuid': 'f776140c-4985-4898-930a-1610441e0345',
    '_shopify_s': '81fa5685-afa2-499d-a51b-f4368e0c1113',
    '_ga_B65Q68TZFY': 'GS2.1.s1759241951$o1$g1$t1759241991$j20$l0$h0',
    '_ga_J3Q1PBV5F9': 'GS2.1.s1759241965$o1$g1$t1759241991$j34$l0$h0',
    '_ga_KSDPC3W2X2': 'GS2.1.s1759241966$o1$g1$t1759241991$j35$l0$h1661330014',
    '_ga_JB1KNT62ST': 'GS2.1.s1759241966$o1$g1$t1759241991$j35$l0$h0',
    '_ga_GZVK1GLZ96': 'GS2.1.s1759241959$o1$g1$t1759241992$j27$l0$h0',
    'cl49824bjrqa63_userSession': '%7B%22sid%22%3A%22CL-19a1faf4-663c-4a1a-b3d5%22%2C%22session_starts%22%3A1759241954882%2C%22session_ends%22%3A1759285192832%7D',
    '_sp_id.d9c8': 'd05099ef-f984-4344-9f3c-c3ff1b984cbe.1759241959.1.1759241993..86a7b108-ac63-4198-bc5f-bba1e4b57f9a..b2df4aed-0490-4b96-a48c-3a47a7dbbc7e.1759241958553.6',
    '_scid_r': '8Ow-YBLtFbGkrdGRJbiNWOpx-uG5GFBI4KCanQ',
    '_uetsid': '7504fa509e0811f0a8a8d7e24063527c|10vv5bz|2|fzr|0|2099',
    '_ks_userCountryUnit': '0',
    '_ks_countryCodeFromIP': 'US',
    '_clsk': '101yhqt%5E1759241993343%5E5%5E1%5Ei.clarity.ms%2Fcollect',
    'cto_bundle': 'IglukF96elo1REVrUzYlMkJvOWtrZ2VvNGl5ZURGdW9Cd2EyeVN2ajdGVjJ5S2lFa3FNRVRwSDQ5bTdJbXZWMGFpSnBIcjdMclExdWlaZjB1ZGZSand3WlN2bThPT1F6NHRSS0pYUzRtekR0dVVIMm8ybSUyQmF6QUF2c2FBNGZBVUx1NFY1JTJGVmtBcXIwSzZVJTJCRUltNW55YkNaOVlReEpmNTNQcWQ1UmREQlVFeDZHaVpwbnp3U05uU2ZuWDZzZkFDa2EwSTVYQg',
    '_ks_scriptVersionChecked': 'true',
    '_ga': 'GA1.2.990949610.1759241952',
    'iDSP_Cookie': 'guid_f43661b0278147a3b0df92d789302225**1759241994382*****',
    'ix_vst': '%7B%22firstVisitTs%22%3A1759241970356%2C%22lastVisitTs%22%3Anull%2C%22currentVisitStartTs%22%3A1759241970356%2C%22ts%22%3A1759241994533%2C%22visitCount%22%3A1%7D',
    '_uetvid': '75053af09e0811f0814cb1b5750c7ea7|u7euvu|1759241994792|6|1|bat.bing.com/p/insights/c/y',
    'kiwi-sizing-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIyODYzNmU5ZC1lYjkxLTRmYjEtYTAyOC03ZmU5MDM5YWUwNjYiLCJpYXQiOjE3NTkyNDE5OTQsImV4cCI6MTc1OTI0NTU5NH0._-Ii36OrOjNM7RWjNi7afChWgrlcMSP-6kzv6wZUSDA',
    'wishlist_id': '7526435bczri3az4jk',
    'bookmarkeditems': '{"items":[]}',
    'wishlist_customer_id': '0',
    'keep_alive': 'eyJ2IjoyLCJ0cyI6MTc1OTI0MjAxNzI1OCwiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjo0MywiY2EiOjIsImthIjo0LCJzYSI6MCwia2JhIjowLCJ0YSI6MCwidCI6MjUsIm5tIjoxLCJtcyI6MC4zOCwibWoiOjAuNjUsIm1zcCI6MC41OSwidmMiOjEsImNwIjowLjI2LCJyYyI6MC4wNywia2oiOjAuOTMsImtpIjozMTI4LjQ1LCJzcyI6MCwic2oiOjAsInNzbSI6MCwic3AiOjAsInRzIjowLCJ0aiI6MCwidHAiOjAsInRzbSI6MH0sInNlcyI6eyJwIjo1LCJzIjoxNzU5MjQxOTUwNTYyLCJkIjo2NH19',
    '_shopify_essential': ':AZma_cV1AAEAuyxKGwK6RPj7JyIp-_T93Acv4LyplwFiOjJ2STnBQmlaRVEKHvWRMxQ-xemRpWfRmP20atg3lblO7SHD2huu7D58nTuvqE9KGvud9tCG-RH68jeBfsUa0tqrK8StATRrkKJrjw4PgbzpGeIfhmGwtRRRAb9oMdPOeK9Eb0QpyCjrVdUHZUbRTOjXSt5cpsWMxJERTPwstRb6xso_qjt_z8MyJAcoNUKraHG63S4FzBgkUBqCVqmSWJS-qbGtgLZV7kSp02dx5LSe0qePO3HN:',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': '"cacheable:a3ec3da7507a7acc9164eace6a5a5e17"',
    'priority': 'u=0, i',
    'referer': 'https://thehouseofrare.com/collections/winter-wear',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': 'localization=IN; _shopify_y=36ada731-e9a9-49eb-adb1-7eef06e9e458; _tracking_consent=3.AMPS_USNJ_f_f_sTSThbj5RcSvyhp3l2-NfA; _orig_referrer=; _landing_page=%2F; fastrr_uuid=cfffde98-a36c-4d79-a363-8c580058a968; fastrr_usid=cfffde98-a36c-4d79-a363-8c580058a968-1759241951857; fastrrPrefetchTriggered=1; _gcl_au=1.1.1420475226.1759241952; __spdt=c7b5d01aa4e74aa8b67208b821edc438; fastrrUserIdEventTriggered=1; cl49824bjrqa63_uid=cl49824bjrqa63d3d434a7-1966-4ae4-b065-b39ea3e35bc7; cl49824bjrqa63_utmParams=%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3A%22Direct%22%7D; cl49824bjrqa63_gid=cl49824bjrqa63c0714956-d3fb-4ab2-a26f-e0dd1618ef33; KP_MERCHANT_CONFIG={"id":131,"merchantId":"19g6ilvf14ycs","name":"Rare rabbit Kwikpass","host":"rarerabbit.myshopify.com","platform":"Shopify","kwikpassEnabled":true,"isWhatsappOtpLessActive":true,"isTruecallerActive":true,"integrationType":"PLUGIN","isLogoutBtnDisabled":false,"popupBreakpoint":"1240px","apiKey":"66c7fb48f170a338f38b7c795b1db597","isPublicAppInstalled":false,"customerIntelligenceEnabled":false,"customerIntelligenceMetrics":null,"marketingPopupGlobalLimit":"1","customerAccountsVersion":"classic","kpAppName":null,"isCustomAccountPageEnabled":false,"isPagePingEnabled":false,"pagePingConfig":null,"thirdPartyServiceProviders":[],"kpRequestId":"faaef8fd-9f6e-447d-be86-f20dd8cfb3e4"}; FP_CONTROLS_DATA={"fpFlowAllowd":false,"vIdGeneration":{"enabled":false,"limitReached":true},"apiConfigurations":{},"generator":""}; _ka_c_ce=%5B%5D; _ka_c=%7B%22isConfigured%22%3Afalse%2C%22standardEvents%22%3A%5B%5D%7D; shopify_api_tags=["KWIKPASS"]; shopify_api_tags_login_modal=["KWIKPASS"]; unbxd.userId=uid-1759241957082-60561; unbxd.visit=first_time; unbxd.visitId=visitId-1759241957090-62095; kp_session_id=5ac9810f-488f-4d92-b415-1ff4b67ea4e1; kp_user_id=01999afd-f31d-707d-96c3-8988e6a94a86; _sp_ses.d9c8=*; SP_DUID=d05099ef-f984-4344-9f3c-c3ff1b984cbe; _scid=4Ww-YBLtFbGkrdGRJbiNWOpx-uG5GFBI; afUserId=51807e91-99b3-4d20-8f69-0d0e30071649-p; AF_SYNC=1759241960336; _ScCbts=%5B%5D; _clck=1yoi1pm%5E2%5Efzr%5E1%5E2099; _gid=GA1.2.1009669663.1759241966; _gat_gtag_UA_63311952_3=1; _gat_UA-63311952-1=1; _fbp=fb.1.1759241969916.301323445438827611; cl49824bjrqa63_eids=%7B%22eids%22%3A%7B%22_shopify_y%22%3A%2236ada731-e9a9-49eb-adb1-7eef06e9e458%22%7D%2C%22eidsTracked%22%3Atrue%7D; _sctr=1%7C1759170600000; imageAnimation=true; moe_uuid=f776140c-4985-4898-930a-1610441e0345; _shopify_s=81fa5685-afa2-499d-a51b-f4368e0c1113; _ga_B65Q68TZFY=GS2.1.s1759241951$o1$g1$t1759241991$j20$l0$h0; _ga_J3Q1PBV5F9=GS2.1.s1759241965$o1$g1$t1759241991$j34$l0$h0; _ga_KSDPC3W2X2=GS2.1.s1759241966$o1$g1$t1759241991$j35$l0$h1661330014; _ga_JB1KNT62ST=GS2.1.s1759241966$o1$g1$t1759241991$j35$l0$h0; _ga_GZVK1GLZ96=GS2.1.s1759241959$o1$g1$t1759241992$j27$l0$h0; cl49824bjrqa63_userSession=%7B%22sid%22%3A%22CL-19a1faf4-663c-4a1a-b3d5%22%2C%22session_starts%22%3A1759241954882%2C%22session_ends%22%3A1759285192832%7D; _sp_id.d9c8=d05099ef-f984-4344-9f3c-c3ff1b984cbe.1759241959.1.1759241993..86a7b108-ac63-4198-bc5f-bba1e4b57f9a..b2df4aed-0490-4b96-a48c-3a47a7dbbc7e.1759241958553.6; _scid_r=8Ow-YBLtFbGkrdGRJbiNWOpx-uG5GFBI4KCanQ; _uetsid=7504fa509e0811f0a8a8d7e24063527c|10vv5bz|2|fzr|0|2099; _ks_userCountryUnit=0; _ks_countryCodeFromIP=US; _clsk=101yhqt%5E1759241993343%5E5%5E1%5Ei.clarity.ms%2Fcollect; cto_bundle=IglukF96elo1REVrUzYlMkJvOWtrZ2VvNGl5ZURGdW9Cd2EyeVN2ajdGVjJ5S2lFa3FNRVRwSDQ5bTdJbXZWMGFpSnBIcjdMclExdWlaZjB1ZGZSand3WlN2bThPT1F6NHRSS0pYUzRtekR0dVVIMm8ybSUyQmF6QUF2c2FBNGZBVUx1NFY1JTJGVmtBcXIwSzZVJTJCRUltNW55YkNaOVlReEpmNTNQcWQ1UmREQlVFeDZHaVpwbnp3U05uU2ZuWDZzZkFDa2EwSTVYQg; _ks_scriptVersionChecked=true; _ga=GA1.2.990949610.1759241952; iDSP_Cookie=guid_f43661b0278147a3b0df92d789302225**1759241994382*****; ix_vst=%7B%22firstVisitTs%22%3A1759241970356%2C%22lastVisitTs%22%3Anull%2C%22currentVisitStartTs%22%3A1759241970356%2C%22ts%22%3A1759241994533%2C%22visitCount%22%3A1%7D; _uetvid=75053af09e0811f0814cb1b5750c7ea7|u7euvu|1759241994792|6|1|bat.bing.com/p/insights/c/y; kiwi-sizing-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIyODYzNmU5ZC1lYjkxLTRmYjEtYTAyOC03ZmU5MDM5YWUwNjYiLCJpYXQiOjE3NTkyNDE5OTQsImV4cCI6MTc1OTI0NTU5NH0._-Ii36OrOjNM7RWjNi7afChWgrlcMSP-6kzv6wZUSDA; wishlist_id=7526435bczri3az4jk; bookmarkeditems={"items":[]}; wishlist_customer_id=0; keep_alive=eyJ2IjoyLCJ0cyI6MTc1OTI0MjAxNzI1OCwiZW52Ijp7IndkIjowLCJ1YSI6MSwiY3YiOjEsImJyIjoxfSwiYmh2Ijp7Im1hIjo0MywiY2EiOjIsImthIjo0LCJzYSI6MCwia2JhIjowLCJ0YSI6MCwidCI6MjUsIm5tIjoxLCJtcyI6MC4zOCwibWoiOjAuNjUsIm1zcCI6MC41OSwidmMiOjEsImNwIjowLjI2LCJyYyI6MC4wNywia2oiOjAuOTMsImtpIjozMTI4LjQ1LCJzcyI6MCwic2oiOjAsInNzbSI6MCwic3AiOjAsInRzIjowLCJ0aiI6MCwidHAiOjAsInRzbSI6MH0sInNlcyI6eyJwIjo1LCJzIjoxNzU5MjQxOTUwNTYyLCJkIjo2NH19; _shopify_essential=:AZma_cV1AAEAuyxKGwK6RPj7JyIp-_T93Acv4LyplwFiOjJ2STnBQmlaRVEKHvWRMxQ-xemRpWfRmP20atg3lblO7SHD2huu7D58nTuvqE9KGvud9tCG-RH68jeBfsUa0tqrK8StATRrkKJrjw4PgbzpGeIfhmGwtRRRAb9oMdPOeK9Eb0QpyCjrVdUHZUbRTOjXSt5cpsWMxJERTPwstRb6xso_qjt_z8MyJAcoNUKraHG63S4FzBgkUBqCVqmSWJS-qbGtgLZV7kSp02dx5LSe0qePO3HN:',
}

# response = requests.get(
#     'https://thehouseofrare.com/collections/winter-wear/products/costo-j-mens-sweatshirt-black',
#     cookies=cookies,
#     headers=headers,
# )
# print(response.status_code)
# print(response.text)


import urllib.parse

token = "f42a5b59aec3467e97a8794c611c436b91589634343"

targetUrl = urllib.parse.quote("https://thehouseofrare.com/collections/winter-wear/products/costo-j-mens-sweatshirt-black")

url = "http://api.scrape.do/?token={}&url={}".format(token, targetUrl)

response = requests.request("GET", url,)
print(response.status_code)
# print(response.text)
print(response.headers)