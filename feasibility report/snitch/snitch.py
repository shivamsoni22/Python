import requests

cookies = {
    '_gcl_au': '1.1.1292149937.1759242671',
    '_ga': 'GA1.1.1429364286.1759242671',
    '_fbp': 'fb.1.1759242674491.47663561513991375',
    'WZRK_G': '5071cf5d5e4e4d5a8da5edcc4892fc30',
    'WZRK_S_8WR-8KR-6K7Z': '%7B%22p%22%3A1%2C%22s%22%3A1759242677%2C%22t%22%3A1759242677%7D',
    '_ga_DNS555JC93': 'GS2.1.s1759242671$o1$g1$t1759242713$j18$l0$h1083448380',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_gcl_au=1.1.1292149937.1759242671; _ga=GA1.1.1429364286.1759242671; _fbp=fb.1.1759242674491.47663561513991375; WZRK_G=5071cf5d5e4e4d5a8da5edcc4892fc30; WZRK_S_8WR-8KR-6K7Z=%7B%22p%22%3A1%2C%22s%22%3A1759242677%2C%22t%22%3A1759242677%7D; _ga_DNS555JC93=GS2.1.s1759242671$o1$g1$t1759242713$j18$l0$h1083448380',
}

# response = requests.get(
#     'https://www.snitch.com/men-jeans/buzzer-black-baggy-fit-jeans/8092596207778/buy',
#     cookies=cookies,
#     headers=headers,
# )



import urllib.parse

# token = "f42a5b59aec3467e97a8794c611c436b91589634343"

targetUrl = urllib.parse.quote("https://www.snitch.com/men-jeans/buzzer-black-baggy-fit-jeans/8092596207778/buy")

url = "http://api.scrape.do/?token={}&url={}".format(token, targetUrl)

response = requests.request("GET", url,)
print(response.status_code)
# print(response.text)
print(response.headers)