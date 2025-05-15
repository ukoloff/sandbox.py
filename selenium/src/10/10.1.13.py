#
# https://stepik.org/lesson/897512/step/13?unit=1066949
#
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/5.10/6/index.html")

    sliders = browser.find_elements(By.CLASS_NAME, "volume-slider")
    targets = browser.find_elements(By.CLASS_NAME, "target-value")

    action = ActionChains(browser)
    action.pause(1).perform()

    for slider, target in zip(sliders, targets):
      target = int(target.text)
      while int(slider.get_attribute('value')) != target:
        slider.send_keys(Keys.LEFT if int(slider.get_attribute('value')) > target else Keys.RIGHT)

    action.pause(1).perform()

    ans = browser.find_element(By.ID, "message")
    print(ans.text)
