#
# https://stepik.org/lesson/897512/step/7?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get("https://parsinger.ru/draganddrop/3/index.html")

    src = browser.find_element(By.ID, "block1")
    dst = browser.find_elements(By.CLASS_NAME, "controlPoint")

    action = ActionChains(browser)
    for z in dst:
      action.drag_and_drop(src, z)
      action.perform()

    action.drag_and_drop(src, dst[0]).perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
