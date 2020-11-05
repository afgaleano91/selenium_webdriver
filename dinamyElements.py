import unittest
from selenium import webdriver
from time import sleep

class DinamycElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "/usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Disappearing Elements").click()

    def testNameElements(self):
        driver = self.driver

        options = []
        menus = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menus):
                try:
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"OPtion number {i + 1} is NOT FOUND")
                    tries +=1
                    driver.refresh()

        print(f"Finished in {tries} tries :D ")

    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()