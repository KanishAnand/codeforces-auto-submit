from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium") 
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://codeforces.com/problemset/problem/1167/G')

options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/kanish/.config/google-chrome/Default")
#w=webdriver.Chrome(executable_path="/home/kanish/chromedriver",chrome_options=options)
w = webdriver.Chrome(chrome_options=options)
w.get('https://codeforces.com/')