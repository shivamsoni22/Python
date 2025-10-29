import requests

cookies = {
    'ai_user': 'UdeC9tN11bZShcdpMvdmGN|2025-10-15T12:49:01.770Z',
    'INGRESSCOOKIE': '1760532543.61.43.625784|37206e05370eb151ee9f1b6a1c80a538',
    'w-rctx': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg',
    'wow-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg',
    'prodwow-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg',
    'at_check': 'true',
    'AMCVS_4353388057AC8D357F000101%40AdobeOrg': '1',
    'AMCV_4353388057AC8D357F000101%40AdobeOrg': '179643557%7CMCIDTS%7C20377%7CMCMID%7C46721066497301145372280532912456970012%7CMCAAMLH-1761137344%7C7%7CMCAAMB-1761137344%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1760539744s%7CNONE%7CvVersion%7C5.5.0',
    'utag_main_v_id': '0199e7eaf7c6001cc3fed52ba3b60506f005f067007e8',
    'utag_main__sn': '1',
    'utag_main_ses_id': '1760532559820%3Bexp-session',
    'fullstoryEnabled': 'false',
    'utag_main_vapi_domain': 'woolworths.com.au',
    'utag_main_dc_visit': '1',
    's_cc': 'true',
    '_pin_unauth': 'dWlkPVlqazRORGsxWlRRdE4yUmhNQzAwWXprNUxXRmhPREV0TVRJek5qYzFaalV4WmpFNQ',
    '_scid': 'I3_StGyhqr4fEb51l-cIpTGEnjVQyvp6',
    'utag_main_dc_region': 'ap-southeast-2%3Bexp-session',
    '_ga': 'GA1.1.1740760740.1760532566',
    'IR_gbd': 'woolworths.com.au',
    '_fbp': 'fb.2.1760532567300.790124579994254140',
    '_tt_enable_cookie': '1',
    '_ttp': '01K7KYP5F2E535ECS4062CXB4S_.tt.2',
    '_ScCbts': '%5B%22332%3Bchrome.2%3A2%3A5%22%2C%22626%3Bchrome.2%3A2%3A5%22%5D',
    '_gcl_au': '1.1.1549310546.1760532568',
    'utag_main_dleUpToDate': 'true%3Bexp-session',
    '_sctr': '1%7C1760466600000',
    'utag_main__ss': '0%3Bexp-session',
    'AKA_A2': 'A',
    'bff_region': 'syd1',
    'bm_mi': 'AC87A06519AE38B3DB7D79461A6E353A~YAAQGkrHF5JpyKOZAQAAZnLr5x0dpvMv0bK+BIb+C2g2fJwcPB8kGWPXOSs0DhjqS9wceQw5NhOmdOWqQFDuwQNdN34Ra97XVJr5CEmLUA80d/384qrAKTOrc7BlUo6VKCp7Yjk3+rrr+ds5dLKzmK8ZhmgG5LL9dG3SvvXWvUNqRGsWQb93G8EqDu+UjnwRLpP6yPbrCN27HZltyn5PdGGZ/Tw9IFo8crClROx0TVA3QWrozispxfxqAhqy7FmMIIOwuqpBJGCuAuGSmMyqy8HzsfCwEKpAbo/PQXA8O48P2qI3jqD2a4lRQsPICCYt6wC+g/s=~1',
    'akaalb_woolworths.com.au': '~op=www_woolworths_com_au_ZoneC:PROD-ZoneC|www_woolworths_com_au_BFF_SYD_Launch:WOW-BFF-SYD|www_woolworths_com_au_ZoneB:PROD-ZoneB|www_woolworths_com_au_BFF_MEL_Launch:WOW-BFF-MEL|~rv=85~m=PROD-ZoneC:0|WOW-BFF-SYD:0|PROD-ZoneB:0|WOW-BFF-MEL:0|~os=43eb3391333cc20efbd7f812851447e6~id=560e3dde851b97cf5e341145a41089ed',
    'rxVisitor': '1760532595291P04UUI48FE7TUCFPQBON0HTDFHHU1O1H',
    'dtSa': '-',
    'ak_bmsc': 'C5E5A5ACA60AB26E030CE275CF0CF445~000000000000000000000000000000~YAAQGkrHF6hqyKOZAQAA6Jnr5x0qdSgd/sdNJAxrJXxDlLFfh43/XWZJ4TH26Q21spxF7NMCVM4mR8mUVyIRfopKU11drLG1JN5kWUj+Y6bmzVGY8uuUcAyKa+4RV/w8riNnEUsgwf4IQJGK4j37mV4jwIioz1jQrzTWa2Es5CbJjoyLqitVV5/pdOiVkFJk7NlDDHWYcOD8niOBDrgey76rzPvkikfsTlMmzEp76HzSFHIPTpg2uhFTxcTL41I7aIGELKmh/W87+JJ/JdhQG29aASYSfkXbxaAe8l55m6ix4aOf03yaBa1/Ykt6+U9YIHXiDftfVBZZGNCb8v55waevubwRVCaFBMAYIl1pc2Bu6y0XqS1EgiYM72290cVEuE1IGsbaOuVztZrz4WSdjjMmcluOAm5B8T8J0NKrOXhle9Qs29Oi3IWZHC/VPe5Dx/zQRZIEo2U0GPbzHGQzCGLTmniiSaYnNJH15fzg1aMNAaJxmM2mkA==',
    'dtCookie': 'v_4_srv_2_sn_C0891B09424781AC929737476DF19533_app-3Af908d76079915f06_1_ol_0_perc_100000_mul_1_rcs-3Acss_0',
    'IR_7464': '1760532616209%7C0%7C1760532616209%7C%7C',
    '_scid_r': 'PP_StGyhqr4fEb51l-cIpTGEnjVQyvp6Ut8V5A',
    'ttcsid_CJ0AT43C77U75407IG80': '1760532567544::m0yUUit7A4gmfx6KhSMn.1.1760532618466.0',
    'ttcsid': '1760532567548::bAmUIzkIKXhkdFKdpK4r.1.1760532618476.0',
    'kampyle_userid': '5f5d-1300-3a73-d03a-804d-2b3d-0398-eddf',
    'kampyleUserSession': '1760532623595',
    'kampyleUserSessionsCount': '1',
    'kampyleUserPercentile': '48.227102551310644',
    'kampyleSessionPageCounter': '2',
    'utag_main_dc_event': '7%3Bexp-session',
    'bm_sz': 'C7ACE6C3A3C6FBE4999CD0E00EB43C98~YAAQGkrHF6dxyKOZAQAAf7Xs5x0uY0teiKB+YPJleiLkWerOxpN4ELp11FHICthLMj3TgMmy8sd7u9KfH7pouk+Xa8FcpqA7kOC2VewzyRdTu421Gft2uxAqkGYqYFge+RBlUrjLt6nM19cCa5OuGGZsvf+G99DFDPw3kq5R5KZwUGzOpFd+8MVQu84IrvjiWAq/JNEB1I290wiMYwAvuXuMi5/N97+yWKx0D1dlTV7k2VCgcgfF5QrkAT+6EsQIoVGif8IJJjZl3sAiEnKMiJbiagV0K4p5eegrb39jUAIFwKGsRwn8X5jNEVPkDPJv5UPxZD4ETZfEFB5qTsklVudfOjtAx/7ujpEONmReiojyacOovX5jVKPGe/XeVq31u589HZ0F20LkfHjq6rpWMZS59pgkZXnSNgD23OWMVPoudORvnmMYd0968j66V1DXPMQvZAVIWLxWof63jw==~4273716~4539715',
    '_ga_YBVRJYN9JL': 'GS2.1.s1760532566$o1$g1$t1760532674$j34$l0$h0',
    'mbox': 'session#9cc4411939f54e9492df531c021238fe#1760534536|PC#9cc4411939f54e9492df531c021238fe.36_0#1823777453',
    'RT': '"z=1&dm=www.woolworths.com.au&si=b8a3342f-3d7e-453a-bafc-ef989cabf117&ss=mgrzma51&sl=2&tt=qhv&obo=1&rl=1"',
    '_abck': '0CA2D9C8C1A2400F21EBCC8AE5C2E859~0~YAAQGkrHF9RxyKOZAQAA3b3s5w5nlDHeFFn6Zm+P9yQqRH4f/OicXHSxpktPNsPTpsEkAE44otxF8FwYmoRLxgDd8fSRyw3GKOuShrG4SG7JCLiM5kqG7qIcSJzCuRMjF8yIhQdk2tkPcXOd0dKwSpplUugYGrEAUEvTYQEwNsurnFRXqjW0N1x1ecxpS45UfvwnwQ76Gm8Zq3kHpSR8PS6NgxH+1DWf2OO4VIqc/0zcC+A85WenyIE//nGoAGy1oOzTVZOYV1QY0iyAKuEovOTfR4gXoE1ylvM1zo+Sxw7TjWDXov674qmZzWHBzzxYgPoGqmyg9Vs3qxC4WHAPMRF2mf1Le7ABcUAywKTa+aNK86tYeLckBwmm2go5mSjw9ETl70f6VeDI3du11S/D14OA8DGHzl8WJlK+wSblCZb5cm+5bCvrYYwW16zAeOWzj7/VNI9VwNgckBm6NBBzTL52nMLsRG7YRfziCFySkSmsAZ4W9T1ZlrBX+wiidfm1MlIawTWUAGNYu2i96YwNBZUMbisbp7ACTmsWuGYjIq72eF5NitPoJoEz/rmAS1VzDfLO+A+mTS3UiqOnFOz4xTPm8t5lZXHuLpnXk7SqGOc7IJxfiBdv0/72Y4g0Apw9/M/oOHbDjzF8lxG/wDCaqcVbLTx105TgvhVHc19ZOIOIYJ3pMAvRd6upAcQRKpLdYm0yXO5kqOBSopEshh1f/Yzu8jje+lyZNBdWSQgjZKxyapmeULTWaVPBEonBUcFlT9Q9hgrmG+ij0oEB1hjFl032NOWRxEGgASzqq1+ZYVcKE1IrPYUYr669YPd3CyANYbUEX7H1OirMT61+Mp2Ti013L6ihnOuk3u+v74KOtXtfsK9UZOmfjee0y7ZPdiCwTTjUor+yaKPO+yd44ciZiCWjUo8ui0WMK+iT/5uMU3xOLCTkezL9n0GfQk6MRZlycpdP+hRd6rg61FOcgZJ09wALq46L9NH7eCemvWcOK9yvDF4vOKH2fMuD~-1~-1~1760536145~AAQAAAAE%2f%2f%2f%2f%2f8hfLq88M07w%2fDZ5WhOdl2eGrpXnQ4YHPH7jNAnvicpn18iFa2AbUryjXs%2fIYFXcvPF5Mt9Gs%2f0ZKxqND8ZaERGUE8AkOwUl6bofA%2fTGi0Yw5+eiignJoRBDfwwYuaF8OgS0coI%3d~-1',
    'ai_session': 'bpNSJhQxSB3OZMUw/CUqxK|1760532542979|1760532677729',
    'utag_main__pn': '3%3Bexp-session',
    'utag_main__se': '11%3Bexp-session',
    'utag_main__st': '1760534479768%3Bexp-session',
    '_uetsid': '608309f0a9c511f0ab9ca516bffba46f',
    '_uetvid': '6083e180a9c511f0824e674395930a3f',
    'bm_sv': '7F5D538F957A57D40AFCA5EB5D4E0FCC~YAAQGkrHF0FyyKOZAQAAedDs5x1okkKl8Dlpagr1Yy2iuC1YYi4Q3dnvbl0WK1nELoxy8pmOgEXuwtBBz1Z62X7lP4jmNFmCONzKDVKWO3jmqquuUPtuGTaQNMyVKMIHWZ44sgzUptX8GlEKk3nyheeprH+hW/CaRfcInJ2UOp1oBUTpHyztqx2G1KPb1Z7ozsoIcCr76gwDf8UJ1oU722Y8ifP3GN5bFW7RN4kVz/SpgSsLn8gE0mkDZsU+TCxrmoJ3Xufz86w=~1',
    'rxvt': '1760534481128|1760532595293',
    'dtPC': '2$132674582_733h33vQPGCHWQFHULPJMGWOORHOOCPVFRIKQPJ-0e0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.woolworths.com.au',
    'priority': 'u=1, i',
    'referer': 'https://www.woolworths.com.au/shop/search/products?searchTerm=Shampoo',
    'request-id': '|b3565226087340cfb3081f93a83f62d9.c931fcb3fad04673',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-b3565226087340cfb3081f93a83f62d9-c931fcb3fad04673-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-dtpc': '2$132674582_733h33vQPGCHWQFHULPJMGWOORHOOCPVFRIKQPJ-0e0, 2$132674582_733h33vQPGCHWQFHULPJMGWOORHOOCPVFRIKQPJ-0e0',
    # 'cookie': 'ai_user=UdeC9tN11bZShcdpMvdmGN|2025-10-15T12:49:01.770Z; INGRESSCOOKIE=1760532543.61.43.625784|37206e05370eb151ee9f1b6a1c80a538; w-rctx=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg; wow-auth-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg; prodwow-auth-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3NjA1MzI1NDIsImV4cCI6MTc2MDUzNjE0MiwiaWF0IjoxNzYwNTMyNTQyLCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6IjJmYTBlZmJlLTljYTUtNDE4My04N2Y5LWFjMDMwZWMxYTFkNiIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.nitfngXYM7uXG0uvUFk_sDApoa6jG3aAbNfIXuc8a-oCgh42DZsfN2QLych0pdz8Gn8stwstkdDxjQI4zISVbtkHxhc2sAPjR8AXtgwsiXIQcrTy5U7tzIbkC9UDSzqdKQjMQ-ZYKCXmT-KZ9OLEOTwAPvWpRP00PFy32oM1fz0Fky7w9a4IBSRyo8IkB0maK9UxTCBsNyaCQw9W3hCze_etdy3GpOsW4tzFVxHQEC04HrlFBYfyCQVFd4ePER1f_xObII6aXCue1fN7_wL8IkLBFmmpMAYQ5pjKEg5L_9JEpIZSXNnGp0V832pkqEUk6O7m8Ua7Gx7BUWiTHGzJNg; at_check=true; AMCVS_4353388057AC8D357F000101%40AdobeOrg=1; AMCV_4353388057AC8D357F000101%40AdobeOrg=179643557%7CMCIDTS%7C20377%7CMCMID%7C46721066497301145372280532912456970012%7CMCAAMLH-1761137344%7C7%7CMCAAMB-1761137344%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1760539744s%7CNONE%7CvVersion%7C5.5.0; utag_main_v_id=0199e7eaf7c6001cc3fed52ba3b60506f005f067007e8; utag_main__sn=1; utag_main_ses_id=1760532559820%3Bexp-session; fullstoryEnabled=false; utag_main_vapi_domain=woolworths.com.au; utag_main_dc_visit=1; s_cc=true; _pin_unauth=dWlkPVlqazRORGsxWlRRdE4yUmhNQzAwWXprNUxXRmhPREV0TVRJek5qYzFaalV4WmpFNQ; _scid=I3_StGyhqr4fEb51l-cIpTGEnjVQyvp6; utag_main_dc_region=ap-southeast-2%3Bexp-session; _ga=GA1.1.1740760740.1760532566; IR_gbd=woolworths.com.au; _fbp=fb.2.1760532567300.790124579994254140; _tt_enable_cookie=1; _ttp=01K7KYP5F2E535ECS4062CXB4S_.tt.2; _ScCbts=%5B%22332%3Bchrome.2%3A2%3A5%22%2C%22626%3Bchrome.2%3A2%3A5%22%5D; _gcl_au=1.1.1549310546.1760532568; utag_main_dleUpToDate=true%3Bexp-session; _sctr=1%7C1760466600000; utag_main__ss=0%3Bexp-session; AKA_A2=A; bff_region=syd1; bm_mi=AC87A06519AE38B3DB7D79461A6E353A~YAAQGkrHF5JpyKOZAQAAZnLr5x0dpvMv0bK+BIb+C2g2fJwcPB8kGWPXOSs0DhjqS9wceQw5NhOmdOWqQFDuwQNdN34Ra97XVJr5CEmLUA80d/384qrAKTOrc7BlUo6VKCp7Yjk3+rrr+ds5dLKzmK8ZhmgG5LL9dG3SvvXWvUNqRGsWQb93G8EqDu+UjnwRLpP6yPbrCN27HZltyn5PdGGZ/Tw9IFo8crClROx0TVA3QWrozispxfxqAhqy7FmMIIOwuqpBJGCuAuGSmMyqy8HzsfCwEKpAbo/PQXA8O48P2qI3jqD2a4lRQsPICCYt6wC+g/s=~1; akaalb_woolworths.com.au=~op=www_woolworths_com_au_ZoneC:PROD-ZoneC|www_woolworths_com_au_BFF_SYD_Launch:WOW-BFF-SYD|www_woolworths_com_au_ZoneB:PROD-ZoneB|www_woolworths_com_au_BFF_MEL_Launch:WOW-BFF-MEL|~rv=85~m=PROD-ZoneC:0|WOW-BFF-SYD:0|PROD-ZoneB:0|WOW-BFF-MEL:0|~os=43eb3391333cc20efbd7f812851447e6~id=560e3dde851b97cf5e341145a41089ed; rxVisitor=1760532595291P04UUI48FE7TUCFPQBON0HTDFHHU1O1H; dtSa=-; ak_bmsc=C5E5A5ACA60AB26E030CE275CF0CF445~000000000000000000000000000000~YAAQGkrHF6hqyKOZAQAA6Jnr5x0qdSgd/sdNJAxrJXxDlLFfh43/XWZJ4TH26Q21spxF7NMCVM4mR8mUVyIRfopKU11drLG1JN5kWUj+Y6bmzVGY8uuUcAyKa+4RV/w8riNnEUsgwf4IQJGK4j37mV4jwIioz1jQrzTWa2Es5CbJjoyLqitVV5/pdOiVkFJk7NlDDHWYcOD8niOBDrgey76rzPvkikfsTlMmzEp76HzSFHIPTpg2uhFTxcTL41I7aIGELKmh/W87+JJ/JdhQG29aASYSfkXbxaAe8l55m6ix4aOf03yaBa1/Ykt6+U9YIHXiDftfVBZZGNCb8v55waevubwRVCaFBMAYIl1pc2Bu6y0XqS1EgiYM72290cVEuE1IGsbaOuVztZrz4WSdjjMmcluOAm5B8T8J0NKrOXhle9Qs29Oi3IWZHC/VPe5Dx/zQRZIEo2U0GPbzHGQzCGLTmniiSaYnNJH15fzg1aMNAaJxmM2mkA==; dtCookie=v_4_srv_2_sn_C0891B09424781AC929737476DF19533_app-3Af908d76079915f06_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; IR_7464=1760532616209%7C0%7C1760532616209%7C%7C; _scid_r=PP_StGyhqr4fEb51l-cIpTGEnjVQyvp6Ut8V5A; ttcsid_CJ0AT43C77U75407IG80=1760532567544::m0yUUit7A4gmfx6KhSMn.1.1760532618466.0; ttcsid=1760532567548::bAmUIzkIKXhkdFKdpK4r.1.1760532618476.0; kampyle_userid=5f5d-1300-3a73-d03a-804d-2b3d-0398-eddf; kampyleUserSession=1760532623595; kampyleUserSessionsCount=1; kampyleUserPercentile=48.227102551310644; kampyleSessionPageCounter=2; utag_main_dc_event=7%3Bexp-session; bm_sz=C7ACE6C3A3C6FBE4999CD0E00EB43C98~YAAQGkrHF6dxyKOZAQAAf7Xs5x0uY0teiKB+YPJleiLkWerOxpN4ELp11FHICthLMj3TgMmy8sd7u9KfH7pouk+Xa8FcpqA7kOC2VewzyRdTu421Gft2uxAqkGYqYFge+RBlUrjLt6nM19cCa5OuGGZsvf+G99DFDPw3kq5R5KZwUGzOpFd+8MVQu84IrvjiWAq/JNEB1I290wiMYwAvuXuMi5/N97+yWKx0D1dlTV7k2VCgcgfF5QrkAT+6EsQIoVGif8IJJjZl3sAiEnKMiJbiagV0K4p5eegrb39jUAIFwKGsRwn8X5jNEVPkDPJv5UPxZD4ETZfEFB5qTsklVudfOjtAx/7ujpEONmReiojyacOovX5jVKPGe/XeVq31u589HZ0F20LkfHjq6rpWMZS59pgkZXnSNgD23OWMVPoudORvnmMYd0968j66V1DXPMQvZAVIWLxWof63jw==~4273716~4539715; _ga_YBVRJYN9JL=GS2.1.s1760532566$o1$g1$t1760532674$j34$l0$h0; mbox=session#9cc4411939f54e9492df531c021238fe#1760534536|PC#9cc4411939f54e9492df531c021238fe.36_0#1823777453; RT="z=1&dm=www.woolworths.com.au&si=b8a3342f-3d7e-453a-bafc-ef989cabf117&ss=mgrzma51&sl=2&tt=qhv&obo=1&rl=1"; _abck=0CA2D9C8C1A2400F21EBCC8AE5C2E859~0~YAAQGkrHF9RxyKOZAQAA3b3s5w5nlDHeFFn6Zm+P9yQqRH4f/OicXHSxpktPNsPTpsEkAE44otxF8FwYmoRLxgDd8fSRyw3GKOuShrG4SG7JCLiM5kqG7qIcSJzCuRMjF8yIhQdk2tkPcXOd0dKwSpplUugYGrEAUEvTYQEwNsurnFRXqjW0N1x1ecxpS45UfvwnwQ76Gm8Zq3kHpSR8PS6NgxH+1DWf2OO4VIqc/0zcC+A85WenyIE//nGoAGy1oOzTVZOYV1QY0iyAKuEovOTfR4gXoE1ylvM1zo+Sxw7TjWDXov674qmZzWHBzzxYgPoGqmyg9Vs3qxC4WHAPMRF2mf1Le7ABcUAywKTa+aNK86tYeLckBwmm2go5mSjw9ETl70f6VeDI3du11S/D14OA8DGHzl8WJlK+wSblCZb5cm+5bCvrYYwW16zAeOWzj7/VNI9VwNgckBm6NBBzTL52nMLsRG7YRfziCFySkSmsAZ4W9T1ZlrBX+wiidfm1MlIawTWUAGNYu2i96YwNBZUMbisbp7ACTmsWuGYjIq72eF5NitPoJoEz/rmAS1VzDfLO+A+mTS3UiqOnFOz4xTPm8t5lZXHuLpnXk7SqGOc7IJxfiBdv0/72Y4g0Apw9/M/oOHbDjzF8lxG/wDCaqcVbLTx105TgvhVHc19ZOIOIYJ3pMAvRd6upAcQRKpLdYm0yXO5kqOBSopEshh1f/Yzu8jje+lyZNBdWSQgjZKxyapmeULTWaVPBEonBUcFlT9Q9hgrmG+ij0oEB1hjFl032NOWRxEGgASzqq1+ZYVcKE1IrPYUYr669YPd3CyANYbUEX7H1OirMT61+Mp2Ti013L6ihnOuk3u+v74KOtXtfsK9UZOmfjee0y7ZPdiCwTTjUor+yaKPO+yd44ciZiCWjUo8ui0WMK+iT/5uMU3xOLCTkezL9n0GfQk6MRZlycpdP+hRd6rg61FOcgZJ09wALq46L9NH7eCemvWcOK9yvDF4vOKH2fMuD~-1~-1~1760536145~AAQAAAAE%2f%2f%2f%2f%2f8hfLq88M07w%2fDZ5WhOdl2eGrpXnQ4YHPH7jNAnvicpn18iFa2AbUryjXs%2fIYFXcvPF5Mt9Gs%2f0ZKxqND8ZaERGUE8AkOwUl6bofA%2fTGi0Yw5+eiignJoRBDfwwYuaF8OgS0coI%3d~-1; ai_session=bpNSJhQxSB3OZMUw/CUqxK|1760532542979|1760532677729; utag_main__pn=3%3Bexp-session; utag_main__se=11%3Bexp-session; utag_main__st=1760534479768%3Bexp-session; _uetsid=608309f0a9c511f0ab9ca516bffba46f; _uetvid=6083e180a9c511f0824e674395930a3f; bm_sv=7F5D538F957A57D40AFCA5EB5D4E0FCC~YAAQGkrHF0FyyKOZAQAAedDs5x1okkKl8Dlpagr1Yy2iuC1YYi4Q3dnvbl0WK1nELoxy8pmOgEXuwtBBz1Z62X7lP4jmNFmCONzKDVKWO3jmqquuUPtuGTaQNMyVKMIHWZ44sgzUptX8GlEKk3nyheeprH+hW/CaRfcInJ2UOp1oBUTpHyztqx2G1KPb1Z7ozsoIcCr76gwDf8UJ1oU722Y8ifP3GN5bFW7RN4kVz/SpgSsLn8gE0mkDZsU+TCxrmoJ3Xufz86w=~1; rxvt=1760534481128|1760532595293; dtPC=2$132674582_733h33vQPGCHWQFHULPJMGWOORHOOCPVFRIKQPJ-0e0',
}

json_data = {
    'Filters': [],
    'IsSpecial': False,
    'Location': '/shop/search/products?searchTerm=Shampoo',
    'PageNumber': 1,
    'PageSize': 36,
    'SearchTerm': 'Shampoo',
    'SortType': 'TraderRelevance',
    'IsRegisteredRewardCardPromotion': None,
    'ExcludeSearchTypes': [
        'UntraceableVendors',
    ],
    'GpBoost': 0,
    'GroupEdmVariants': False,
    'EnableAdReRanking': False,
}

response = requests.post('https://www.woolworths.com.au/apis/ui/Search/products', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"Filters":[],"IsSpecial":false,"Location":"/shop/search/products?searchTerm=Shampoo","PageNumber":1,"PageSize":36,"SearchTerm":"Shampoo","SortType":"TraderRelevance","IsRegisteredRewardCardPromotion":null,"ExcludeSearchTypes":["UntraceableVendors"],"GpBoost":0,"GroupEdmVariants":false,"EnableAdReRanking":false}'
#response = requests.post('https://www.woolworths.com.au/apis/ui/Search/products', cookies=cookies, headers=headers, data=data)
MONGO_URI = "mongodb://localhost:27017/"  # apne MongoDB URI yaha add karo
DB_NAME = "woolworths_db"
COLLECTION_NAME = "products"

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
print("✅ MongoDB Connected Successfully")

# ===== Step 1: Create folders for HTML storage =====
HTML_DIR = "saved_html"
os.makedirs(HTML_DIR, exist_ok=True)



shiabk,ka slinala xz  all()