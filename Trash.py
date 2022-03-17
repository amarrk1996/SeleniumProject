import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings

warnings.filterwarnings("ignore")

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
# driver.get('https://courses.microdegree.work/users/sign_in')
#time.sleep(2)
un_ele=driver.find_element_by_xpath('//*[@id="user[email]"]')
print(un_ele.is_displayed()) #checks if element is displayed or not, returns TRUE/FALSE
print(un_ele.is_enabled()) #checks if element is enabled or not, returns TRUE/FALSE
pw_ele=driver.find_element_by_name(name="user[password]")
#time.sleep(2)
print(pw_ele.is_enabled())
print(pw_ele.is_displayed())
un_ele.send_keys('amarrkayapure@gmail.com')
pw_ele.send_keys('Kayapure@18')
driver.find_element_by_xpath('/html/body/main/div/div/article/form/div[4]/input').click()