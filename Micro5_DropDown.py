import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/forms.html')
driver.maximize_window()
Select(driver.find_element_by_id('state')).select_by_visible_text('Tamilnadu')
time.sleep(1)
Select(driver.find_element_by_id('state')).select_by_index(1)
time.sleep(1)
Select(driver.find_element_by_id('state')).select_by_value('karnataka')
# Length of the dropdownlist
print(len(Select(driver.find_element_by_id('state')).options))
statelist=Select(driver.find_element_by_id('state')).options
for all_state in statelist:
    print(all_state.text)
print(statelist)
# print(statelist.text) 'list' object has no attribute 'text'
driver.quit()