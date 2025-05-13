#
# https://stepik.org/lesson/779274/step/2?unit=781792
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
    browser.get("https://parsinger.ru/selenium/7/7.4.1/index.html")

    ActionChains(browser).scroll_by_amount(0, 1200).perform()
    ActionChains(browser).pause(3.5).perform()
    cd = browser.find_element(By.CLASS_NAME, 'countdown').text
    cd = cd.split()[-1]
    print(cd)
    ActionChains(browser).scroll_by_amount(0, 2400).perform()
    inp = browser.find_element(By.TAG_NAME, 'input')
    inp.clear()
    inp.send_keys(cd)
    browser.find_element(By.TAG_NAME, 'button').click()


    ans = browser.find_element(By.ID, 'final-key').text
    print(ans)
