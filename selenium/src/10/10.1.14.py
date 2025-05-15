#
# https://stepik.org/lesson/897512/step/14?unit=1066949
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

svc = webdriver.ChromeService(
    executable_path=r"C:\Users\s.ukolov\.cache\selenium\chromedriver\win64\135.0.7049.114\chromedriver.exe"
)

with webdriver.Chrome(service=svc) as browser:
    browser.implicitly_wait(1)
    browser.get("https://parsinger.ru/draganddrop/4/index.html")

    word = browser.find_element(By.ID, 'target-word').text
    slots = browser.find_elements(By.CLASS_NAME, "letter-slot")
    letters = browser.find_elements(By.CLASS_NAME, "draggable-letter")
    idx = dict((z.text, z) for z in letters)

    action = ActionChains(browser)
    action.pause(1).perform()

    for slot, letter in zip(slots, word):
      src = idx[letter]
      action.drag_and_drop(src, slot).perform()

    action.pause(1).perform()

    ans = browser.find_element(By.ID, "password")
    print(ans.text)
