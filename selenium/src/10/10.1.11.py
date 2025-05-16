#
# https://stepik.org/lesson/897512/step/11?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.get("https://parsinger.ru/selenium/5.10/4/index.html")
    browser.fullscreen_window()

    action = ActionChains(browser)
    action.pause(1).perform()

    # src = browser.find_elements(By.CLASS_NAME, "ball_color")
    for dst in browser.find_elements(By.CLASS_NAME, "basket_color"):
       for klass in dst.get_attribute('class').split():
          for src in browser.find_elements(By.CLASS_NAME, klass + "_ball"):
            action.drag_and_drop(src, dst)
            action.perform()

    ans = browser.find_element(By.CLASS_NAME, "message")
    print(ans.text)
