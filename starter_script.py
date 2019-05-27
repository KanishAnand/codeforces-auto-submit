from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options=webdriver.ChromeOptions()

##################################### CHANGES TO BE MADE HERE #############################################################
options.add_argument("user-data-dir=/home/kanish/.config/google-chrome/Default")
driver = webdriver.Chrome(executable_path='/home/kanish/Documents/chromedriver/chromedriver',chrome_options=options)
###########################################################################################################################

driver.get("https://codeforces.com/")

#written by : Kanish Anand