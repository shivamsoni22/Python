import requests

cookies = {
    'dtCookie': 'v_4_srv_6_sn_670FE162344BD639F13FBF3B57F2F0CA_perc_100000_ol_0_mul_1_app-3Ac92d1dc9fc213bbd_0',
    '_gcl_au': '1.1.1290374327.1759225440',
    '_am.p13n': '4f457e79-abdb-79eb-7f6d-c1a3a1a47f9c',
    '_ga': 'GA1.1.357266143.1759225441',
    '_uetsid': '005c45109de211f0b70ff99be4ddc915',
    '_uetvid': '005c80309de211f0995edd0ae07d6dc5',
    'c_fid': 'b22936fbed2641c3cb821699ce0976c6447e',
    'oppuz_session': '%2268dba664263a7cc7de685f6e%22',
    '_fbp': 'fb.2.1759225446301.570178790369452592',
    '_pin_unauth': 'dWlkPU5tTmlZMlk0WWpBdE0yVTJaQzAwWlRRekxXRTJObU10TkRBMVl6a3pOak5tT0dNMA',
    '_clck': 'f1ot5s%5E2%5Efzr%5E0%5E2099',
    'FPC': 'id=fa391690-6398-47ae-b321-a0b65be4e5ad',
    'AwinChannelCookie': 'direct',
    'WTPERSIST': 'product=air',
    'cf_clearance': 'Iqr2YEmHXEGB9zEP4V.DIW7z8_Z3mIRTIaH98y6Jy0g-1759229916-1.2.1.1-G8nkpMhfaJ3mNgJQ8lV7hHsK1rEbqX6cUk.0IKmN0LQzwKtHODzV.B8tCnGYtF2ZFAzzF.PUmnt8aTJwwAKFUuR1GEbYyvVVEqxseWIaFtQsLYtbhNUG5yRlVGT0z32AEXfgzGwXbVonyvUTdX3Zk6SPQuGeSgLYDjmTt.MF5Z8ZxO5FzpISkXST_sDhX8xMrQJxCqt2J.TUjODBoRsnxR74usr71rvYbmbBRGqqawc',
    '_am.session_id': 'a57a84e4-c8fb-581e-c949-71d9eaf60b6e',
    '__cf_bm': 'ESTe1TSeWlVOksLHtETHWRHTaHt8DcTrSbosKlRciBs-1759230856-1.0.1.1-UbDH96DvHh1JZMcNklN0jKQcRImSuJa8GiqwvoBW86qUu3F8smXpHRG8ulCU7q5w2Om8R9uuPm.IlIpSUW6no2o1vjWLBZLmlv2EbOOzq60',
    '__eoi': 'ID=47a2fd71c419dc89:T=1759225448:RT=1759230860:S=AA-AfjZww14clVgsKg3NjiWx_br9',
    'BIGipServer~PROD~pool_merged_site_cvc_hosting_-_http': 'rd10o00000000000000000000ffffac103e71o80',
    '_tt_enable_cookie': '1',
    '_ttp': '01K6D59N2MT9KB3TCHAH5A25RK_.tt.2',
    'ttcsid': '1759230874717::HAIBTjNmuiHa_r4Yhoup.1.1759230876342.0',
    'ttcsid_C9BG1IJC77U9N0P9DR10': '1759230874715::nwfFS9QX0oDL5vw_lTFz.1.1759230876342.0',
    'referrer': 'www.cvc.com.br',
    '_ga_YJE8M07CX7': 'GS2.1.s1759229921$o2$g1$t1759230921$j60$l0$h1212391469',
    '_ga_SFPDWB4X9Y': 'GS2.1.s1759229921$o2$g1$t1759230921$j60$l0$h0',
    '_ga_FBQMH9TYN2': 'GS2.1.s1759229923$o2$g1$t1759230923$j59$l0$h0',
    'cto_bundle': '_t9DEF9ZaGJkM0tIOEx5diUyRmVvWXlkeVIlMkJxTUh5eDBBbEhJc0xLT2pIemNLWmVONlVvUVZ2Rk05bzNvdWJkSmZMUzVIWlFrJTJGbnlXdWQxdTdOSnUyZUZVenE3dGVGblhKT1VVRE9WMUdZSUw1NVNMdGtFRkpBVlRaVnoyRUgwcVZHM093cTVWZXFpQmd4bDRkWlJ6OVNVUlRQeDVSNjRERXdaOUFTT2lFeXFoaTI0MmVXNCUyQkVWNTdsTUcwVFh4dCUyRkhTamxx',
    '_clsk': '1bstkw3%5E1759230924461%5E8%5E1%5Eb.clarity.ms%2Fcollect',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-allow-origin': '*',
    'content-type': 'application/json',
    'origin': 'https://www.cvc.com.br',
    'priority': 'u=1, i',
    'referer': 'https://www.cvc.com.br/passagens/v2/search/VCP/POA?fType=roundtrip&CLA=all&ADT=1&CHD=0&INF=0&MCO1=Aeroporto%20Internacional%20Viracopos,%20Campinas,%20Brasil%20(VCP)&MCD1=Aeroporto%20Internacional%20Salgado%20Filho,%20Porto%20Alegre,%20Brasil%20(POA)&Date1=2025-10-12&Date2=2025-10-25&STO=PACKAGE',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"140.0.7339.208"',
    'sec-ch-ua-full-version-list': '"Chromium";v="140.0.7339.208", "Not=A?Brand";v="24.0.0.0", "Google Chrome";v="140.0.7339.208"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'transactionid': '69191260-6e88-49cc-b148-26ecbabda455',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'x-api-version': '3.0',
    'x-dtpc': '6$30919075_943h20vPHNBWRNGMFMAIAJWWPSESPRUCVPHMCUN-0e0',
    'x-instana-l': '1,correlationType=web;correlationId=bb486a20f09d95c1',
    'x-instana-s': 'bb486a20f09d95c1',
    'x-instana-t': 'bb486a20f09d95c1',
    # 'cookie': 'dtCookie=v_4_srv_6_sn_670FE162344BD639F13FBF3B57F2F0CA_perc_100000_ol_0_mul_1_app-3Ac92d1dc9fc213bbd_0; _gcl_au=1.1.1290374327.1759225440; _am.p13n=4f457e79-abdb-79eb-7f6d-c1a3a1a47f9c; _ga=GA1.1.357266143.1759225441; _uetsid=005c45109de211f0b70ff99be4ddc915; _uetvid=005c80309de211f0995edd0ae07d6dc5; c_fid=b22936fbed2641c3cb821699ce0976c6447e; oppuz_session=%2268dba664263a7cc7de685f6e%22; _fbp=fb.2.1759225446301.570178790369452592; _pin_unauth=dWlkPU5tTmlZMlk0WWpBdE0yVTJaQzAwWlRRekxXRTJObU10TkRBMVl6a3pOak5tT0dNMA; _clck=f1ot5s%5E2%5Efzr%5E0%5E2099; FPC=id=fa391690-6398-47ae-b321-a0b65be4e5ad; AwinChannelCookie=direct; WTPERSIST=product=air; cf_clearance=Iqr2YEmHXEGB9zEP4V.DIW7z8_Z3mIRTIaH98y6Jy0g-1759229916-1.2.1.1-G8nkpMhfaJ3mNgJQ8lV7hHsK1rEbqX6cUk.0IKmN0LQzwKtHODzV.B8tCnGYtF2ZFAzzF.PUmnt8aTJwwAKFUuR1GEbYyvVVEqxseWIaFtQsLYtbhNUG5yRlVGT0z32AEXfgzGwXbVonyvUTdX3Zk6SPQuGeSgLYDjmTt.MF5Z8ZxO5FzpISkXST_sDhX8xMrQJxCqt2J.TUjODBoRsnxR74usr71rvYbmbBRGqqawc; _am.session_id=a57a84e4-c8fb-581e-c949-71d9eaf60b6e; __cf_bm=ESTe1TSeWlVOksLHtETHWRHTaHt8DcTrSbosKlRciBs-1759230856-1.0.1.1-UbDH96DvHh1JZMcNklN0jKQcRImSuJa8GiqwvoBW86qUu3F8smXpHRG8ulCU7q5w2Om8R9uuPm.IlIpSUW6no2o1vjWLBZLmlv2EbOOzq60; __eoi=ID=47a2fd71c419dc89:T=1759225448:RT=1759230860:S=AA-AfjZww14clVgsKg3NjiWx_br9; BIGipServer~PROD~pool_merged_site_cvc_hosting_-_http=rd10o00000000000000000000ffffac103e71o80; _tt_enable_cookie=1; _ttp=01K6D59N2MT9KB3TCHAH5A25RK_.tt.2; ttcsid=1759230874717::HAIBTjNmuiHa_r4Yhoup.1.1759230876342.0; ttcsid_C9BG1IJC77U9N0P9DR10=1759230874715::nwfFS9QX0oDL5vw_lTFz.1.1759230876342.0; referrer=www.cvc.com.br; _ga_YJE8M07CX7=GS2.1.s1759229921$o2$g1$t1759230921$j60$l0$h1212391469; _ga_SFPDWB4X9Y=GS2.1.s1759229921$o2$g1$t1759230921$j60$l0$h0; _ga_FBQMH9TYN2=GS2.1.s1759229923$o2$g1$t1759230923$j59$l0$h0; cto_bundle=_t9DEF9ZaGJkM0tIOEx5diUyRmVvWXlkeVIlMkJxTUh5eDBBbEhJc0xLT2pIemNLWmVONlVvUVZ2Rk05bzNvdWJkSmZMUzVIWlFrJTJGbnlXdWQxdTdOSnUyZUZVenE3dGVGblhKT1VVRE9WMUdZSUw1NVNMdGtFRkpBVlRaVnoyRUgwcVZHM093cTVWZXFpQmd4bDRkWlJ6OVNVUlRQeDVSNjRERXdaOUFTT2lFeXFoaTI0MmVXNCUyQkVWNTdsTUcwVFh4dCUyRkhTamxx; _clsk=1bstkw3%5E1759230924461%5E8%5E1%5Eb.clarity.ms%2Fcollect',
}

json_data = {
    'searchCacheKey': 'search_results_369104d6-d3fc-43b7-9d5c-5c49055016a2',
    'uids': [
        'lKSxWx75zUWpIYu+6wFQ3Q',
        'ms5GiKCpL0O+Y4ZaTir8YA',
        'Ag2dX08CREqiO+47BzH8WA',
        'ssJj0Md5r0+fIarON0QDYw',
    ],
}

# response = requests.post(
#     'https://www.cvc.com.br/api/flights/Search/GetCachedSearchResultsFiltered',
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )

# # Note: json_data will not be serialized by requests
# # exactly as it was in the original request.
# data = '{"searchCacheKey":"search_results_369104d6-d3fc-43b7-9d5c-5c49055016a2","uids":["lKSxWx75zUWpIYu+6wFQ3Q","ms5GiKCpL0O+Y4ZaTir8YA","Ag2dX08CREqiO+47BzH8WA","ssJj0Md5r0+fIarON0QDYw"]}'
# response = requests.post(
#    'https://www.cvc.com.br/api/flights/Search/GetCachedSearchResultsFiltered',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
import requests

import urllib.parse

token = "f42a5b59aec3467e97a8794c611c436b91589634343"

targetUrl = urllib.parse.quote("https://www.cvc.com.br/api/flights/Search/GetCachedSearchResultsFiltered")

url = "http://api.scrape.do/?token={}&url={}".format(token, targetUrl)

response = requests.request("GET", url,data=json_data,headers=headers,cookies=cookies)

print(response.text)
print(response.status_code)
print(response.text)