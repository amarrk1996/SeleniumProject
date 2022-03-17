from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/forms.html')
driver.find_element_by_id('gender-male').click()
print(driver.find_element_by_id('gender-male').is_enabled())
print(driver.find_element_by_id('gender-male').is_selected())
print(driver.find_element_by_id('gender-male').is_displayed())
driver.find_element_by_id('music').click()
print(driver.find_element_by_id('music').is_enabled())
print(driver.find_element_by_id('music').is_selected())
print(driver.find_element_by_id('music').is_displayed())
