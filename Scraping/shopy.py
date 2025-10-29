import requests

cookies = {
    'T': 'nnc8lq7aojk6nkdqlilh0ubl-BR1759140048724',
    'DC_ID': '2',
    'vw': '1280',
    'ud': '1.LVZrK_aI6l96C8UBmMy-zBHz5O8hCGlBvUysqbfOfe4DeiZouuw-uilKcxd-SOjNsGJP4z5KScmXWkMPrSm4iw',
    '_gcl_au': '1.1.1879272254.1759140060',
    '_ga': 'GA1.1.211638197.1759140060',
    'vd': 'VI49C7B1277AC14988B6F6F2715A62A91B-1759140048906-3.1759211531.1759210753.152831797',
    'S': 'd1t18aSk/QQoNQm4/Zz8/FD9gPwm6cwbfLFK/NEVhdQWoCnomSrXiLEKUcKK/IOLV09oJmYQC7ZEUq8zE5CbyprL8+Q==',
    'at': '',
    'K-ACTION': '',
    'SN': 'VI49C7B1277AC14988B6F6F2715A62A91B.TOK1496274528DD48ABB6CBEE3FE240B23F.1759211538.LO',
    '_ga_MF2PJ1ME3R': 'GS2.1.s1759210758$o4$g1$t1759211552$j59$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version': '"140.0.7339.208"',
    'sec-ch-ua-full-version-list': '"Chromium";v="140.0.7339.208", "Not=A?Brand";v="24.0.0.0", "Google Chrome";v="140.0.7339.208"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    # 'cookie': 'T=nnc8lq7aojk6nkdqlilh0ubl-BR1759140048724; DC_ID=2; vw=1280; ud=1.LVZrK_aI6l96C8UBmMy-zBHz5O8hCGlBvUysqbfOfe4DeiZouuw-uilKcxd-SOjNsGJP4z5KScmXWkMPrSm4iw; _gcl_au=1.1.1879272254.1759140060; _ga=GA1.1.211638197.1759140060; vd=VI49C7B1277AC14988B6F6F2715A62A91B-1759140048906-3.1759211531.1759210753.152831797; S=d1t18aSk/QQoNQm4/Zz8/FD9gPwm6cwbfLFK/NEVhdQWoCnomSrXiLEKUcKK/IOLV09oJmYQC7ZEUq8zE5CbyprL8+Q==; at=; K-ACTION=; SN=VI49C7B1277AC14988B6F6F2715A62A91B.TOK1496274528DD48ABB6CBEE3FE240B23F.1759211538.LO; _ga_MF2PJ1ME3R=GS2.1.s1759210758$o4$g1$t1759211552$j59$l0$h0',
}

params = {
    'pid': 'XSNGEFQYFANN6B2S',
    'lid': 'LSTXSNGEFQYFANN6B2S8XKNU0',
    'marketplace': 'FLIPKART',
    'store': 'osp',
}

response = requests.get(
    'https://www.shopsy.in/men-black-sandals/p/itm4651c67c1825e',
    params=params,
    cookies=cookies,
    headers=headers,
)