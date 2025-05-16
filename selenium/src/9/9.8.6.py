#
# https://stepik.org/lesson/732083/step/6?unit=733616
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.9/4/index.html")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "closeBtn"))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.ID, "closeBtn"))
    )

    browser.find_element(By.TAG_NAME, 'button').click()
    ans = browser.find_element(By.ID, 'message').text
    print(ans)
