import requests

cookies = {
    '__cf_bm': 'J9sD.WbnCQY5CAly23OLIjUfNvZRw2f2hP33kWxHwZM-1759232009-1.0.1.1-3d8QDRJIr48JKBOZ_YpLnCZeq1rZsvvFl11Y6W5T_F3PqRNMF5.sqTkdNUbHiavlwF2XAtr0nFxLoVTQgH9dauGbfeqRUIC8iQ0anbi2gxA',
    'xdesp-rand-usr': '600',
    'trackerid': '338be4fc-bdb4-4d4d-963f-fab8c9753992',
    'tracker_context': 'fallback_error',
    'trackerid': '338be4fc-bdb4-4d4d-963f-fab8c9753992',
    'AwinChannelCookie': 'organic',
    '_gcl_au': '1.1.1790714831.1759232015',
    '_gid': 'GA1.2.1942738871.1759232017',
    '_fbp': 'fb.1.1759232017182.148566564358293341',
    '_tt_enable_cookie': '1',
    '_ttp': '01K6D6CH3D957FH8R6G0P8TC32_.tt.1',
    '__gads': 'ID=74a100d5ce85ab9c:T=1759232017:RT=1759232017:S=ALNI_MZmyAickellbYMGTrhR1m9Hh6GiDg',
    '__gpi': 'UID=0000119cce60b165:T=1759232017:RT=1759232017:S=ALNI_MZXdZPaZt3sVXjx7oh85vX5Npe34w',
    '__eoi': 'ID=e4503571b0097c25:T=1759232017:RT=1759232017:S=AA-AfjY8g6jJU_wH5AAUySct_Was',
    '_clck': '1bbvvpv%5E2%5Efzr%5E0%5E2099',
    '__sessionId_cookie': '1d212ac9bebb582c4f3b991bf4ad2ffe',
    'x-locale': 'pt-BR',
    'previousUrl': 'https://www.decolar.com/shop/flights/results/roundtrip/AMD/SAO/2025-10-01/2025-10-10/1/0/0?from=SB&di=1',
    'trackeame_cookie': '%7B%22id%22%3A%22338be4fc-bdb4-4d4d-963f-fab8c9753992%22%2C%22upa_id%22%3A%22338be4fc-bdb4-4d4d-963f-fab8c9753992%22%2C%22creation_date%22%3A%222025-09-30T11%3A34%3A43Z%22%2C%22company_id%22%3A%221%22%2C%22version%22%3A%227.0%22%7D',
    '_hjSessionUser_3595196': 'eyJpZCI6IjQ3NmQ4ODBjLWNjMGYtNTFhNS1hYTVjLTJmZDQ3ZmZkNWFkOSIsImNyZWF0ZWQiOjE3NTkyMzIwODcwNTYsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjSession_3595196': 'eyJpZCI6ImE1ZWZlYzIzLTQ0MjEtNDc0ZS1hMjBjLTgyNDdmMWI2MzUxZiIsImMiOjE3NTkyMzIwODcwNTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22dsui5H6rLdCKi8JeW6tE%22%2C%22expiryDate%22%3A%222026-09-30T11%3A34%3A48.517Z%22%7D',
    '_uetsid': '4e0e52109df111f0a786e5512e1c1040',
    '_uetvid': '4e1375e09df111f09299c38e3897f47c',
    '_ga': 'GA1.2.255680194.1759232016',
    'X-hide-value-proposition-results': 'true',
    '_ga_XXXXXXXXXX': 'GS2.1.s1759232017$o1$g1$t1759232094$j48$l0$h1739071021',
    '_ga_JKEBDBGYXJ': 'GS2.1.s1759232015$o1$g1$t1759232095$j47$l0$h994585628',
    '_clsk': '9txh85%5E1759232096809%5E4%5E0%5Eb.clarity.ms%2Fcollect',
    'datadome': 'Nhh1fFoMn3HZmsN2zRpKsskQzFxPgvtAW~xpDbOmcHY0Ng1cF6jicZBcXgUqgcKV0faDLzwYwl9aXbmNla2mqJDx5jQgIlJGXD_ugRP6NJxt6cKoH51EwdEJ8V3WEg2~',
    'ttcsid': '1759232017528::BL_aOfEB0Tj8OyYBfi1b.1.1759232120480.0',
    'ttcsid_CMSIT3JC77U755R2RV50': '1759232017524::kJfGsJlU6CsP-QgybrdX.1.1759232120480.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.decolar.com/',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Chromium";v="140.0.7339.208", "Not=A?Brand";v="24.0.0.0", "Google Chrome";v="140.0.7339.208"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': '__cf_bm=J9sD.WbnCQY5CAly23OLIjUfNvZRw2f2hP33kWxHwZM-1759232009-1.0.1.1-3d8QDRJIr48JKBOZ_YpLnCZeq1rZsvvFl11Y6W5T_F3PqRNMF5.sqTkdNUbHiavlwF2XAtr0nFxLoVTQgH9dauGbfeqRUIC8iQ0anbi2gxA; xdesp-rand-usr=600; trackerid=338be4fc-bdb4-4d4d-963f-fab8c9753992; tracker_context=fallback_error; trackerid=338be4fc-bdb4-4d4d-963f-fab8c9753992; AwinChannelCookie=organic; _gcl_au=1.1.1790714831.1759232015; _gid=GA1.2.1942738871.1759232017; _fbp=fb.1.1759232017182.148566564358293341; _tt_enable_cookie=1; _ttp=01K6D6CH3D957FH8R6G0P8TC32_.tt.1; __gads=ID=74a100d5ce85ab9c:T=1759232017:RT=1759232017:S=ALNI_MZmyAickellbYMGTrhR1m9Hh6GiDg; __gpi=UID=0000119cce60b165:T=1759232017:RT=1759232017:S=ALNI_MZXdZPaZt3sVXjx7oh85vX5Npe34w; __eoi=ID=e4503571b0097c25:T=1759232017:RT=1759232017:S=AA-AfjY8g6jJU_wH5AAUySct_Was; _clck=1bbvvpv%5E2%5Efzr%5E0%5E2099; __sessionId_cookie=1d212ac9bebb582c4f3b991bf4ad2ffe; x-locale=pt-BR; previousUrl=https://www.decolar.com/shop/flights/results/roundtrip/AMD/SAO/2025-10-01/2025-10-10/1/0/0?from=SB&di=1; trackeame_cookie=%7B%22id%22%3A%22338be4fc-bdb4-4d4d-963f-fab8c9753992%22%2C%22upa_id%22%3A%22338be4fc-bdb4-4d4d-963f-fab8c9753992%22%2C%22creation_date%22%3A%222025-09-30T11%3A34%3A43Z%22%2C%22company_id%22%3A%221%22%2C%22version%22%3A%227.0%22%7D; _hjSessionUser_3595196=eyJpZCI6IjQ3NmQ4ODBjLWNjMGYtNTFhNS1hYTVjLTJmZDQ3ZmZkNWFkOSIsImNyZWF0ZWQiOjE3NTkyMzIwODcwNTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3595196=eyJpZCI6ImE1ZWZlYzIzLTQ0MjEtNDc0ZS1hMjBjLTgyNDdmMWI2MzUxZiIsImMiOjE3NTkyMzIwODcwNTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22dsui5H6rLdCKi8JeW6tE%22%2C%22expiryDate%22%3A%222026-09-30T11%3A34%3A48.517Z%22%7D; _uetsid=4e0e52109df111f0a786e5512e1c1040; _uetvid=4e1375e09df111f09299c38e3897f47c; _ga=GA1.2.255680194.1759232016; X-hide-value-proposition-results=true; _ga_XXXXXXXXXX=GS2.1.s1759232017$o1$g1$t1759232094$j48$l0$h1739071021; _ga_JKEBDBGYXJ=GS2.1.s1759232015$o1$g1$t1759232095$j47$l0$h994585628; _clsk=9txh85%5E1759232096809%5E4%5E0%5Eb.clarity.ms%2Fcollect; datadome=Nhh1fFoMn3HZmsN2zRpKsskQzFxPgvtAW~xpDbOmcHY0Ng1cF6jicZBcXgUqgcKV0faDLzwYwl9aXbmNla2mqJDx5jQgIlJGXD_ugRP6NJxt6cKoH51EwdEJ8V3WEg2~; ttcsid=1759232017528::BL_aOfEB0Tj8OyYBfi1b.1.1759232120480.0; ttcsid_CMSIT3JC77U755R2RV50=1759232017524::kJfGsJlU6CsP-QgybrdX.1.1759232120480.0',
}

params = {
    'from': 'SB',
    'di': '1',
}

response = requests.get(
    'https://www.decolar.com/shop/flights/results/roundtrip/AMD/SAO/2025-10-01/2025-10-10/1/0/0',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(response.text)

