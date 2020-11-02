import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        #tiempos de espera

    def testSearchfield(self):
        self.assertTrue(self.isElementPresent(By.NAME, 'q'))

    def testLanguage(self):
        self.assertTrue(self.isElementPresent(By.ID, 'select-language'))
    
    def tearDown(self):
        self.driver.quit()
    
    def isElementPresent(self, how, what):
        try:
            self.driver.find_elements(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True