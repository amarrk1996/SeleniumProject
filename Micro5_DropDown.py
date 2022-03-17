from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
driver=webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get('')