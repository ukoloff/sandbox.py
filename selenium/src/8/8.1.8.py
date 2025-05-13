#
# https://stepik.org/lesson/732076/step/8?unit=733609
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/selenium/8/8.1.2/index.html")

    urls = [a.get_attribute('href') for a in browser.find_elements(By.TAG_NAME, 'a')]
    for url in urls:
        browser.switch_to.new_window('tab:' + url)
        browser.get(url)

    ActionChains(browser).pause(3).perform()

    ans = int(t1) + int(t2)
    print(ans)
