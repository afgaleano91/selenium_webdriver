import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Typos").click()

    def testFindTypo(self):
        driver = self.driver

        paragraphToCheck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        textToCheck = paragraphToCheck.text
        
        self.assertTrue(textToCheck, paragraphToCheck)

        tries = 1
        found = False
        correctText = "Sometimes you'll see a typo, other times you won't."

        while textToCheck != correctText:
            paragraphToCheck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            textToCheck = paragraphToCheck.text
            driver.refresh()
        
        while not found:
            if textToCheck == correctText:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f"It Took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)        