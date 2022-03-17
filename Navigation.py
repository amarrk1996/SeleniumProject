import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")


driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.usertesting.com/get-paid-to-test')
print(driver.title)
driver.get('http://demo.automationtesting.in/Windows.html')
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(5)
driver.close()

