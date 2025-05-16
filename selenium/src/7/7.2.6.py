#
# https://stepik.org/lesson/732066/step/6?unit=733599
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
    browser.get("https://parsinger.ru/selenium/7/7.2/index.html")

    browser.find_element(By.TAG_NAME, "input").click()
    n = 0
    while n < len(browser.find_elements(By.TAG_NAME, "input")):
        n += 1
        ActionChains(browser).send_keys(n).send_keys(Keys.ENTER).send_keys(Keys.DOWN).perform()

    ans = browser.find_element(By.ID, 'hidden-password').text
    print(ans)
