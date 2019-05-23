from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  
import pickle
driver = webdriver.Chrome()
driver.get('https://codeforces.com/problemset/problem/1167/G')
#time.sleep(35)
#pickle.dump(driver.get_cookies(),open("cookies.pkl","wb"))
print("DFd")
for cookie in pickle.load(open("cookies.pkl","rb")):
	print(cookie)
	driver.add_cookie(cookie)
#js=document.querySelector('[name="sourceFile"]').value='C:\\fakepath\\1155B.cpp';
print("FDd")
#driver.execute_script("document.querySelector('[name='sourceFile']').value='C:\\fakepath\\1155B.cpp'")
dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']");
dropFileArea.send_keys('/home/kanish/codeforces/41B.cpp');
driver.find_element_by_xpath("//input[@value='Submit']").click();