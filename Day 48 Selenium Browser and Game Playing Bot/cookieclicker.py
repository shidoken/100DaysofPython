from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys
import time

timeout = time.time() + 10
five_min = time.time() + 60 * 5  # 5 minutes

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_btn = driver.find_element_by_xpath("//*[@id='bigCookie']")


while True:
    cookie_btn.click()
    # get all available items in the store
    items = driver.find_elements_by_class_name("product.unlocked.enabled")
    # Every 5 seconds:
    if time.time() > timeout and len(items) > 0:
        items[len(items) - 1].click()
        # Add 5 seconds
        timeout = time.time() + 10
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_css_selector("#cookies div")
        print(cookie_per_s.text)
        break


#
# cookie_count = driver.find_element_by_id('money').text
#
# items = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment',
#          'buyFactory', 'buyGrandma', 'buyCursor']
#
# while True:
#     cookie.click()
#
#     # items in the store
#     items = driver.find_elements_by_css_selector("#store div")
#     item_ids = [item.get_attribute("id") for item in items]
#
#     # prices in the store
#     all_prices = driver.find_elements_by_css_selector("#store b")
#     item_prices = []
#
#     for price in all_prices:
#         element_text = price.text
#         if element_text != "":
#             cost = int(element_text.split("-")[1].strip().replace(",", ""))
#             item_prices.append(cost)
#
#     # getting all the upgrades
#     cookie_upgrades = {}
#     for n in range(len(item_prices)):
#         cookie_upgrades[item_prices[n]] = item_ids[n]
#
#     # current cookie count
#     money_element = driver.find_element_by_id("money").text
#     if "," in money_element:
#         money_element = money_element.replace(",", "")
#     cookie_count = int(money_element)
#
#     # checking affordable upgrades
#     affordable_upgrades = {}
#     for cost, id in cookie_upgrades.items():
#         if cookie_count > cost:
#             affordable_upgrades[cost] = id
#
#     # Purchase the most expensive affordable upgrade
#     highest_price_affordable_upgrade = max(affordable_upgrades)
#     print(highest_price_affordable_upgrade)
#     to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#     driver.find_element_by_id(to_purchase_id).click()
#
#     # Add another 5 seconds until the next check
#     timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break
#
#     # for i in range(len(items), 0, -1):
#     #     try:
#     #         driver.find_element_by_id(items[i]).click()
#     #     except:
#     #         pass
#     # print(cookie_count)
#     # return
#
#     # every 5 seconds:
#     # if time.time() > timeout:
#     #     test()
#     # count+=1