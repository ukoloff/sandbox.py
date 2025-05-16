#
# https://stepik.org/lesson/732067/step/8?unit=733600
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
    browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")

    el = browser.find_element(By.ID, 'context-area')
    ActionChains(browser).context_click(el).perform()
    el = browser.find_element(By.CSS_SELECTOR, '[data-action=get_password]')
    el.click()

    ans = browser.find_element(By.CSS_SELECTOR, '[key=access_code]').text
    print(ans)
