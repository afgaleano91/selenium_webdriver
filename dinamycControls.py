import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "/usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Dynamic Controls").click()

    def testDynamicControls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox')
        checkbox.click()

        removeAddButton = driver.find_element_by_css_selector('#checkbox-example > button')
        removeAddButton.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))

        enabledDisabledButton = driver.find_element_by_css_selector('#input-example > button')
        enabledDisabledButton.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        textArea = driver.find_element_by_css_selector('#input-example > input[type=text]')
        textArea.send_keys('Automatizacion prro :V ')

        enabledDisabledButton.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()