from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")

driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.marutisuzuki.com/')
driver.find_element_by_xpath("//*[@id='BaSV-Home-red']").click()
print(driver.find_element_by_id('lad-footer').text)
driver.find_element_by_id('lad-footer').click()
# driver.implicitly_wait(5)
# driver.quit()