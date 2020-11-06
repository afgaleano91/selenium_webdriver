import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(('dress', 6), ('music', 5))
    @unpack

    def testSearchDDT(self, search_value, expected_count):
        driver = self.driver

        searchField = driver.find_element_by_name('q')
        searchField.clear()
        searchField.send_keys(search_value)
        searchField.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'se encontro {len(products)}')

        for product in products:
            print(product.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)