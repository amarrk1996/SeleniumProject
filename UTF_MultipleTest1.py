import unittest
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

class SearchEngineTitleName(unittest.TestCase):

    def test1_googleTitleTest(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://www.google.com/')
        print('Title of the Google is '+self.driver.title)
        self.driver.close()

    def test2_yahooTitleTest(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://in.search.yahoo.com/?fr2=inr')
        print('Title of the Yahoo is ' + self.driver.title)
        self.driver.close()

if __name__=='--main__':
    unittest.main()

