#
# https://stepik.org/lesson/897512/step/12?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.10/8/index.html")

    src = browser.find_elements(By.CLASS_NAME, "piece")
    dst = browser.find_elements(By.CLASS_NAME, "range")

    action = ActionChains(browser)
    action.pause(1).perform()

    for p, q in zip(src, dst):
      action.drag_and_drop(p, q)
      action.perform()

    action.pause(1).perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
