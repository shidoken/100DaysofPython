from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException
import random

PROMISED_DOWN = 100
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        options = Options()
        options.add_argument("window-size=1000,800")
        self.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)
        self.wait = WebDriverWait(self.driver, 40)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element_by_class_name('start-text').click()

        speed_tester_progress = ".overall-progress"
        download_speed_css = ".download-speed"
        upload_speed_css = ".upload-speed"
        in_progress = True
        while in_progress:
            progress = self.driver.find_element_by_css_selector(speed_tester_progress).text
            if progress.startswith("Your speed test has completed"):
                download_result = self.driver.find_element_by_css_selector(download_speed_css)
                upload_result = self.driver.find_element_by_css_selector(upload_speed_css)
                print(f"Your download speed is {download_result.text} MBit/s and your upload speed is {upload_result.text} MBit/s")
                self.down = download_result.text
                self.up = upload_result.text
                in_progress = False

            else:
                sleep(5)

    def quotes(self):
        file = '/run/media/tom/Bonus/Linux Files/projects/quotes.txt'
        with open(file, "r") as data:
            self.quote = data.readlines()
        self.the_line = random.choices(self.quote)


    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        login = self.driver.find_element_by_link_text('Log in').click()
        sleep(2)
        username = self.driver.find_element_by_name('session[username_or_email]')
        username.send_keys(USER)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        post_box = self.driver.find_element_by_css_selector('div.public-DraftStyleDefault-block')
        post_box.send_keys(self.the_line)
        tweet_button = self.driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']").click()


tweet = InternetSpeedTwitterBot()
# tweet.get_internet_speed()
# tweet.tweet_at_provider()
tweet.quotes()
tweet.tweet_at_provider()
