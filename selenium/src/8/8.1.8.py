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

    ActionChains(browser).pause(7).perform()

    summa = 0
    for h in browser.window_handles[1:]:
        browser.switch_to.window(h)
        summa += sum(int(z.text) for z in browser.find_elements(By.CLASS_NAME, 'number'))

    browser.switch_to.window(browser.window_handles[0])
    inp = browser.find_element(By.TAG_NAME, 'input')
    inp.clear()
    inp.send_keys(summa)
    browser.find_element(By.TAG_NAME, 'button').click()
    ActionChains(browser).pause(0.3).perform()
    ans = browser.find_element(By.ID, 'passwordDisplay').text
    print(ans)
