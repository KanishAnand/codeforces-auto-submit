from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

#select your language from options given below and paste that to this language variable removing given GNU G++17 7.3.0 and please don't remove double inverted commas("")

####################################### LANGUAGE #####################################################
language = "GNU G++17 7.3.0"
#####################################################################################################
# GNU GCC C11 5.1.0								# Delphi 7					
# Clang++17 Diagnostics							# Free Pascal 3.0.2
# GNU G++11 5.1.0								# PascalABC.NET 3.4.2
# GNU G++14 6.4.0								# Perl 5.20.1
# GNU G++17 7.3.0								# PHP 7.2.13
# Microsoft Visual C++ 2010						# Python 2.7.15
# Microsoft Visual C++ 2017						# Python 3.7.2
# C# Mono 5.18									# PyPy 2.7 (6.0.0)
# D DMD32 v2.083.1								# PyPy 3.5 (6.0.0)
# Go 1.11.4										# Ruby 2.0.0p645
# Haskell GHC 8.6.3								# Rust 1.31.1
# Java 1.8.0_162								# Scala 2.12.8
# Kotlin 1.3.10									# JavaScript V8 4.8.0
# OCaml 4.02.1									# Node.js 9.4.0


#problem code

print("Enter problem code eg : if problem is 1167G type 1167G")
problem=""
problem=input()

l=len(problem)
part1 = problem[0:l-1]
part2 = problem[l-1:l]
st = part1 + '/' + part2
print('https://codeforces.com/problemset/problem/' + st)
#path of code

print("Enter relative path of your code to submit from current directory of the script eg. 1167G.cpp")
pth=os.getcwd()
pt=input()
pth = pth + '/' +  pt
print(pth)

#to get stored profile


################################################### CHANGES TO BE MADE HERE  #####################################################
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/kanish/.config/google-chrome/Default")
driver = webdriver.Chrome(executable_path='/home/kanish/Documents/chromedriver/chromedriver',chrome_options=options)
##################################################################################################################################

#open the link

#if you want to submit your code to some other link then you can change the link below to link where you want to submit your code.
driver.get('https://codeforces.com/problemset/problem/' + st)

#for selecting language

js="var op = document.getElementsByTagName('option');for(var i=0;i<op.length;i++){if(op[i].innerHTML == arguments[0]){op[i].setAttribute('selected','selected');}}"
driver.execute_script(js,language)

#to submit file

dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']");
dropFileArea.send_keys(pth);
driver.find_element_by_xpath("//input[@value='Submit']").click();

#written by : Kanish Anand