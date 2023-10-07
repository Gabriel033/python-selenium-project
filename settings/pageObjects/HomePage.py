from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    menuCuentas = (By.ID, "nav-link-accountList-nav-line-1")
    identificarseButton = (By.XPATH, "//span[contains(text(),'Identificarse')]")
    buscarProductoInputtext = (By.ID, "twotabsearchtextbox")
    buscarProductoButton = (By.ID, "nav-search-submit-button")
    logoAmazon = (By.ID, "nav-logo-sprites")

    def move_to_MenuCuentas(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*HomePage.menuCuentas)
        actions.move_to_element(element).perform()

    def click_in_dentificarse_button(self):
        self.driver.find_element(*HomePage.identificarseButton).click()

    def type_product_search(self, product):
        self.driver.find_element(*HomePage.buscarProductoInputtext).send_keys(str(product))

    def click_product_search(self):
        self.driver.find_element(*HomePage.buscarProductoButton).click()

    def wait_until_logo_amazon_is_present(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*HomePage.logoAmazon]))