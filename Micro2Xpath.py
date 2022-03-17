import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")

driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/selector.html')
# root element > target element
# absolute xpath
driver.find_element_by_xpath('/html/body/center/form/input[1]').send_keys('Amar')
driver.find_element_by_xpath('//input').send_keys('Kayapure')
driver.find_element_by_xpath('//*[@id="your_name"]').clear()
driver.find_element_by_xpath('//*[@class="nameclass"]').send_keys('NewText')
driver.find_element_by_xpath('//form/input[@class="emailclass"]').send_keys('NewText2')
# relative xpath
# //*[@id="your_name"]


