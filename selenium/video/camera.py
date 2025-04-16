from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument("--proxy-server=socks5://localhost:1080")
with webdriver.Chrome(options=opts) as browser:
  browser.implicitly_wait(5)

  browser.get("http://192.168.0.21")

  print(browser)
