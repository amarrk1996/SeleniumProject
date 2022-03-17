from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)
import warnings
warnings.filterwarnings("ignore")

#driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe') #This statement launch the application
driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver-v0.30.0-win64\geckodriver')
#driver=webdriver.Ie(executable_path='C:\Drivers\IEDriverServer_Win32_4.0.0\IEDriverServer.exe')
#like java we don't have system.setproperty method in py.We have to create only driver object

#1st method
driver.get('https://www.usertesting.com/get-paid-to-test')
print(driver.title)        #Show the title of the page
print(driver.current_url)  #Returns current URL of the page
print(driver.page_source)  #Returns HTML codeof the current URL
driver.close()             #close the browser