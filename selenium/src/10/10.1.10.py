#
# https://stepik.org/lesson/897512/step/10?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.10/3/index.html")

    src = browser.find_elements(By.CLASS_NAME, "draganddrop")
    dst = browser.find_elements(By.CLASS_NAME, "draganddrop_end")

    action = ActionChains(browser)
    action.pause(1).perform()

    for p, q in zip(src, dst):
      action.drag_and_drop(p, q)
      action.perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
