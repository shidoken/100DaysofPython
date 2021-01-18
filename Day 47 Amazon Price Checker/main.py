import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'
headers = {
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
title = " ".join(soup.find('span', class_='product-title-word-break').text.split())
price = soup.find('span', class_='priceBlockBuyingPriceString').getText()
set_price = float(price.split('$')[1])

if set_price < 200:
    print(f"{title} is less than $200 and it's at ${set_price} right now.")
    print(f"Go check it out at : {url}")
