from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
driver=webdriver.Chrome()
driver.get("http://codeforces.com")
set<Cookie> cookiesInstance1 = driver.manage().getCookies();
for cookie in cookiesInstance1:
	driver.manage().addCookie(cookie)
