import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")

driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/')
# print(driver.title)
# print(driver.current_url)
# link1 = driver.find_element_by_id('selenium-tutorials-button').text
# if link1== 'Automation Testing Selenium':
#     print('Test successful')
# else:
#     print('Test failed')
# driver.find_element_by_id('selenium-tutorials-button').click()
# selurl=driver.current_url
# if  selurl== 'https://practice.microdegree.work/selenium.html':
#     print('Test successful')
# else:
#     print('Test failed')
# print(driver.pr)
#driver.close()
# driver.find_element_by_partial_link_text('C').click()
driver.find_element_by_id('selenium-tutorials-button').click()
driver.find_element_by_link_text('Locators Practice').click()
# .class_name
driver.find_element_by_css_selector('input.nameclass').send_keys('AmarKing')
# #id
driver.find_element_by_css_selector('input#your_email').send_keys('amarrkayapure@gmail.com')
# driver.find_element_by_tag_name('a').click()
#for tag name elements
driver.find_element_by_css_selector('div div a').click()
driver.find_element_by_css_selector('div div a:nth-child(2)').click()
# driver.quit() #Closes all the tabs