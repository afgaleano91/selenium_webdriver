import unittest
from selenium import webdriver

class homePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= '/usr/bin/chromedriver')
        driver = self.driver
        #tiempos de espera
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
    
    def testSearchTee(self):
        driver = self.driver
        searchField = driver.find_elements_by_name('q')
        searchField.clear()

        searchField.send_keys('tee')
        searchField.submit()

    def testSearchSaltShaker(self):
        driver = self.driver
        searchField = driver.find_elements_by_name('q')

        searchField.send_keys('salt')
        searchField.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    def testSearchTextField(self):
        # Busqueda de elemento
        searchField = self.driver.find_element_by_id('search')

    def testSearchTextFieldByName(self):
        searchField = self.driver.find_element_by_name('q')

    def testSearchTextFieldByClassName(self):
        searchField = self.driver.find_elements_by_class_name('input-text')

    def testSearchButton(self):
        SearchButton = self.driver.find_elements_by_class_name('button')
    
    def testCountOfPromoBannerImages(self):
        banner_list = self.driver.find_elements_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def testVipPromo(self):
        vipPromo = self.driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[2]/a/img')

    def testShoppingCart(self):
        shoppingCartIcon = self.driver.find_elements_by_css_selector("div.header-minicart span.icon")

    
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)