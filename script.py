from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#select your language from options given below and paste that to this language variable removing given c++.

language = "Microsoft Visual C++ 2017"

print("Enter problem number eg : if problem is 1167G type 1167G")
problem=""
problem=input()

#if you want to submit your code to some other link then you can change the link below to link where you want to submit your code.

l=len(problem)
part1 = problem[0:l-1]
part2 = problem[l-1:l]
st = part1 + '/' + part2
print("Enter path of your code to submit eg. /home/kanish/codeforces/1167G.cpp")
pth=input()

options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/kanish/.config/google-chrome/Default")
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://codeforces.com/problemset/problem/' + st)

js="var op = document.getElementsByTagName('option');for(var i=0;i<op.length;i++){if(op[i].innerHTML == arguments[0]){op[i].setAttribute('selected','selected');}}"
driver.execute_script(js,language)

dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']");
dropFileArea.send_keys(pth);
driver.find_element_by_xpath("//input[@value='Submit']").click();