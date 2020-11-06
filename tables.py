import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Sortable Data Tables").click()

    def testSortTables(self):
        driver = self.driver
        tableData = list()

        # Obtengo una lista de los tr en el body de la tabla
        # a dicha lista le aplico un len() y obtenermos cuantos datos hay en el body
        data_size = driver.find_elements_by_xpath('//*[@id="table1"]/tbody/tr')

        # Obtener una lista de los th contenido en el thead de la tabla
        # Con la lista de los th, le aplico un len a la lista y veos cuantos header hay
        header_size = driver.find_elements_by_xpath('//*[@id="table1"]/thead/tr/th')
        

        for i in range(1,len(data_size)+1):
            for j in range(1,len(header_size)): # Omitimos el header action
                header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j}]/span').text
                content = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i}]/td[{j}]').text
                tableData.append({header:content})

        print(tableData)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)      