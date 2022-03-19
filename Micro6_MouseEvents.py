from selenium import webdriver
from selenium.webdriver import ActionChains
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('https://www.selenium.dev/')
driver.maximize_window()
# For Right Click
ActionChains(driver).context_click().perform()
rm1=driver.find_element_by_xpath("//span[@class='navbar-logo']//*[name()='svg']")
ActionChains(driver).context_click(rm1).perform()
driver.quit()
