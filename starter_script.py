from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/kanish/.config/google-chrome/Default")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://codeforces.com/")