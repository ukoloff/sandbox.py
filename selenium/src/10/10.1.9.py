#
# https://stepik.org/lesson/897512/step/9?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(10)
    browser.get("https://parsinger.ru/draganddrop/2/index.html")

    src = browser.find_element(By.ID, "draggable")
    dst = browser.find_elements(By.CLASS_NAME, "box")

    action = ActionChains(browser)
    for z in dst:
      action.drag_and_drop(src, z)
      action.perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
