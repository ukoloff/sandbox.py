#
# https://stepik.org/lesson/897512/step/8?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get("https://parsinger.ru/selenium/5.10/2/index.html")

    src = browser.find_elements(By.CLASS_NAME, "draganddrop")
    dst = browser.find_element(By.CLASS_NAME, "draganddrop_end")

    action = ActionChains(browser)
    for z in src:
      action.drag_and_drop(z, dst)
      action.perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
