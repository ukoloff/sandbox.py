#
# https://stepik.org/lesson/732067/step/7?unit=733600
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(5)
    browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")

    ActionChains(browser).key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('T').key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).perform()

    ans = browser.find_element(By.CSS_SELECTOR, 'span[key=access_code]').text
    print(ans)
