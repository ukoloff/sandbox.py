#
# https://stepik.org/lesson/897512/step/6?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/draganddrop/1/index.html")

    src = browser.find_element(By.ID, "draggable")
    dst = browser.find_element(By.ID, "field2")

    ActionChains(browser).drag_and_drop(src, dst).perform()

    ans = browser.find_element(By.ID, "result")
    print(ans.text)
