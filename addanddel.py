import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        """
        configuracion de driver para poder ejecutar el navegador
        """
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elementsAdd = int(input('How many elements will you add?: '))
        elementsRemove= int(input('How many elements will you remove?: '))
        totalElements = elementsAdd - elementsRemove

        addButton = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elementsAdd):
            addButton.click()
        
        for i in range(elementsRemove):
            try:
                deleteButton = driver.find_element_by_class_name('added-manually')
                deleteButton.click()
            except:
                print("You're trying to delete more elements the that existent")
                break
        if totalElements > 0:
            print(f"There are {totalElements} elements on screen")
        else:
            print('There 0 are elements on screen')

        sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)