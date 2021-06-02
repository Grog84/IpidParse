from urllib.request import urlopen, Request
# import requests

# r = requests.get("https://www.dnb.com/business-directory/company-profiles.34bigthings_srl.a0afafb424d5824e9e5fb9722827673e.html")
# print(r.text)

dnburl = 'https://www.crunchbase.com/organization/uber'

headers = {
    "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
    "Connection": 'keep-alive',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'it,en-US;q=0.9,en;q=0.8,it-IT;q=0.7',
    "Cache-Control": 'max-age=0',
    "Referer": 'https://www.crunchbase.com/organization/uber',
    "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    'Upgrade-Insecure-Requests': '1'
}

req = Request(url=dnburl, headers=headers)
page = urlopen(dnburl)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

# title_index = html.find("<title>")
# print(title_index)

# start_index = title_index + len("<title>")
# end_index = html.find("</title>")

# title = html[start_index:end_index]
# print(title)