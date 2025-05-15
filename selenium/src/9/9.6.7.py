#
# https://stepik.org/lesson/1121332/step/7?unit=1132820
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/9/9.6.3/index.html")

    img = WebDriverWait(browser, 100).until(
        EC.text_to_be_present_in_element_attribute(
            (By.TAG_NAME, "img"), "src", "success"
        )
    )
    browser.find_element(By.TAG_NAME, "img").click()

    ans = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print(ans.text)
