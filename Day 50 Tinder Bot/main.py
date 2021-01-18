from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException

# login info for tinder
EMAIL = os.environ.get('TINDER_EMAIL')
PASSWORD = os.environ.get('TINDER_PW')

# preload stuff
options = Options()
options.add_argument("window-size=1200,500")
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)

# driver.set_window_position(0, 0)
driver.get('https://tinder.com/')

# log in
base_window = driver.window_handles[0]

login_button = driver.find_elements_by_tag_name('button')
login_button[1].click()
sleep(2)
google_login = driver.find_element_by_css_selector('#modal-manager > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(1) > div > button').click()

google_window = driver.window_handles[1]
driver.switch_to.window(google_window)

email_input = driver.find_element_by_css_selector('#identifierId')
email_input.send_keys(EMAIL)
email_input.send_keys(Keys.ENTER)
sleep(2)
password_input = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)
allow = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
enable = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

# going through the cycle of clicking on the profiles
for _ in range(5):
    sleep(1)

    try:
        print('called')
        nope_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()
    except NoSuchElementException:
        sleep(2)
