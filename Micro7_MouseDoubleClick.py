from selenium import webdriver
from selenium.webdriver import ActionChains
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://practice.microdegree.work/doubleclick.html')
driver.maximize_window()
dclick=driver.find_element_by_xpath('/html/body/div[2]/button')
print(dclick.text)
action=ActionChains(driver)
action.double_click(dclick).perform()
# driver.quit()