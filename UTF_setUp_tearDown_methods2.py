import unittest
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

class SearchEngineTitleName(unittest.TestCase):

# decorators
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
    @classmethod
    def tearDown(self) -> None:
        self.driver.close()

    def test1_googleTitleTest(self):
        self.driver.get('https://www.google.com/')
        print('Title of the Google is '+self.driver.title)

    def test2_yahooTitleTest(self):
        self.driver.get('https://in.search.yahoo.com/?fr2=inr')
        print('Title of the Yahoo is ' + self.driver.title)

    def test3_duckduckgoTitleTest(self):
        self.driver.get('https://duckduckgo.com/')
        print('Title of the duckduckgo is ' + self.driver.title)

    def test4_bingTitleTest(self):
        self.driver.get('https://www.bing.com/')
        print('Title of the bing is ' + self.driver.title)

    def test5_askTitleTest(self):
        self.driver.get('https://www.ask.com/')
        print('Title of the ask is ' + self.driver.title)


if __name__=='--main__':
    unittest.main()

