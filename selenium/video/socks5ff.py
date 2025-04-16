from selenium import webdriver

opts = webdriver.ChromeOptions()
# opts.add_argument("--proxy-server=socks5://localhost:1080")
with webdriver.Firefox() as browser:
  browser.implicitly_wait(5)

  browser.get("https://nc.ekb.ru/omz/test/")

  print(browser)
