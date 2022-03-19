from selenium import webdriver
from selenium.webdriver import ActionChains
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/draganddrop2.html')
driver.maximize_window()
source=driver.find_element_by_id('draggable')
target=driver.find_element_by_id('droppable')
action=ActionChains(driver)
action.drag_and_drop(source,target).perform()