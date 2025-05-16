#
# https://stepik.org/lesson/732069/step/8?unit=733602
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/7/7.5/index.html")

    d = browser.find_element(By.CSS_SELECTOR, "body > div")
    cnt = 0
    while True:
        ActionChains(browser).send_keys_to_element(d, Keys.END).pause(0.3).perform()
        z = len(d.find_elements(By.CSS_SELECTOR, ":scope > *"))
        if z == cnt:
            break
        cnt = z

    for z in d.find_elements(By.CLASS_NAME, "like-btn"):
        z.click()

    ans = sum(int(z.text) for z in d.find_elements(By.CLASS_NAME, "big-number"))
    print(ans)
