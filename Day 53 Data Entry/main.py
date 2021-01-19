import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

url = 'https://www.zillow.com/los-angeles-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22los%20angeles%22%2C%22mapBounds%22%3A%7B%22west%22%3A-119.04070028515626%2C%22east%22%3A-117.78276571484376%2C%22south%22%3A33.6759310304271%2C%22north%22%3A34.365690961385205%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A906416%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D'

gsheets = 'https://docs.google.com/forms/d/e/1FAIpQLScx1ap6XuecHzg7BXXaLvVolYM0sZeQRaeVhxmAuHGkE1MRlg/viewform?usp=sf_link'

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# grabbing page data
links = soup.select('.list-card-info a')
price = soup.select('.list-card-price')
address = soup.select('.list-card-info a')

# parsing links
list_links = []
for i in links:
    if 'https://www.zillow.com' not in i.get('href'):
        list_links.append(f"https://www.zillow.com{i.get('href')}")
    else:
        list_links.append(i.get('href'))

# adding prices to the list
list_prices = []
for i in price:
    if " " in i.text:
        list_prices.append(i.text.split()[0])
    else:
        list_prices.append(i.text)

# adding addresses
address = soup.select('.list-card-info a')
list_addresses = []
for i in address:
    list_addresses.append(i.text)

# going to sheets
driver = webdriver.Chrome()
driver.get(gsheets)


def form_fill(fill_address, fill_price, fill_link):
    fill1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill1.send_keys(fill_address)
    fill2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill2.send_keys(fill_price)
    fill3 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill3.send_keys(fill_link)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
    sleep(1)
    another = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

sleep(4)
for i in range(len(links)):
    sleep(1)
    form_fill(list_addresses[i], list_prices[i], list_links[i])
