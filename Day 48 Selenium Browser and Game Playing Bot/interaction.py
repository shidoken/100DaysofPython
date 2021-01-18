from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
#
# article_count = driver.find_element_by_css_selector('#articlecount > a:nth-child(1)')
# # print(article_count.text)
#
# # all_portals = driver.find_element_by_link_text("All portals").click()
#
# search = driver.find_element_by_name('search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get('https://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element_by_name('fName')
first_name.send_keys('Test')
last_name = driver.find_element_by_name('lName')
last_name.send_keys('Ease')
email = driver.find_element_by_name('email')
email.send_keys("test@ease.com")
email.send_keys(Keys.ENTER)