import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore")

driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver-v0.30.0-win64\geckodriver')
driver.maximize_window()
driver.get('https://demo.guru99.com/test/newtours/')
time.sleep(2)
print(driver.title)
print(driver.current_url)
uname=driver.find_element_by_name('userName')
if uname.is_displayed()==True:
    print('User Name field is displayed')
else:
    print('User Name field is not displayed')
print(uname.is_enabled())
pw=driver.find_element_by_name('password')
if pw.is_enabled()!=False:
    print('Password field is Enabled')
else:
    print('Password field is not Enabled')
uname.send_keys('amarrkayapure@gmail.com')
pw.send_keys('Kayapure@18')
driver.find_element_by_xpath("//input[@name='submit']").click()
print('clicked on submit button')
time.sleep(2)

driver.find_element_by_xpath("//a[normalize-space()='Flights']").click()
print('clicked on flight button')
time.sleep(3)
Round_trip= driver.find_element_by_css_selector("input[value='roundtrip']")
# Round_trip= driver.find_element_by_xpath("//input[@value='roundtrip']")
print('Radio button is displayed :', Round_trip.is_displayed())
print('Radio button is enabled :', Round_trip.is_enabled())

#driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a').click()
#driver.find_element_by_xpath("//*[@name='findFlights']").click()
#roundtrip=driver.find_element_by_xpath("//input[@value='roundtrip']")
#print('status of round trip radio button ',roundtrip.is_selected())
#oneway=driver.find_element_by_css_selector('input[value=oneway]')
#print('status of oneway radio button ',oneway.is_selected())
#time.sleep(2)

driver.quit()