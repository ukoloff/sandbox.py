#
# https://stepik.org/lesson/732067/step/9?unit=733600
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
    browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")

    for d in browser.find_elements(By.CLASS_NAME, 'scroll-container'):
      ActionChains(browser).send_keys_to_element(d, Keys.END).perform()

    ActionChains(browser).pause(0.3).perform()

    ans = browser.find_element(By.CSS_SELECTOR, '[key=access_code]').text
    print(ans)
