from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
PHONE = phone_number

# preload stuff
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)

# driver.set_window_position(0, 0)
driver.set_window_size(1200, 1000)
driver.get('https://www.linkedin.com/jobs/search/?f_CF=f_WRA&f_LF=f_AL&keywords=python%20developer')

# signing in
sign_in = driver.find_element_by_link_text('Sign in').click()
sleep(3)
email = driver.find_element_by_id('username')
email.send_keys(EMAIL)
password = driver.find_element_by_id('password')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
sleep(3)

# check the first job, if it fits, apply.
job_card = driver.find_elements_by_css_selector(".job-card-container--clickable")
# job_card = driver.find_elements_by_class_name('jobs-search-results__list-item')
# job_card[0].click()
# job_title = job_card[0].find_element_by_class_name('artdeco-entity-lockup__title').text
# if 'Python' in job_title:
#     sleep(1)
#     apply_button = driver.find_element_by_class_name('jobs-apply-button--top-card').click()
#     sleep(1)
#     next_button = driver.find_element_by_xpath('//*[@data-control-name="continue_unify"]').click()
#     sleep(1)
#     next_button = driver.find_element_by_xpath('//*[@data-control-name="continue_unify"]').click()
# else:
#     # submit_button = driver.find_element_by_xpath('//*[@data-control-name="submit_unify"]').click()
#     print('done with the script')
#     pass

for card in job_card:
    print("called")
    card.click()
    sleep(1)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        sleep(2)
        # if phone field is empty, fill with phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss").click()
            sleep(1)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
            print("Complex application, skipped.")
            continue
        else:
            print('submit button press')
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss").click()
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
            # submit_button.click()

        # Once application completed, close the pop-up window.
        sleep(1)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss").click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
    continue

# sleep(5)
# driver.quit()
