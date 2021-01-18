from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver.get('https://www.python.org/')
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_data = {}

for i in range(5):
    time = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time').text
    name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a').text
    case = {'time': time, 'name': name}
    event_data[i] = case

print(event_data)


# driver.close()
driver.quit()