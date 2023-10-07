from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    primerProducto = (By.XPATH, "(//span[contains(text(),'Resultados')]//following::div[@class='a-section aok-relative s-image-square-aspect']/img[not(contains(@src,'01siZb3GpxL.png')) and not(contains(@alt,'Topari Juego de Cartas'))])[1]")
    resultados_title = (By.XPATH, "//span[contains(text(),'Resultados')]")

    def wait_until_result_is_present(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*SearchPage.resultados_title]))

    def scroll_first_product(self):
        element = self.driver.find_element(*SearchPage.primerProducto)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_first_product(self):
        self.driver.find_element(*SearchPage.primerProducto).click()
