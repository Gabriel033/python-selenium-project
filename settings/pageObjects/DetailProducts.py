from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DetailProducts:

    def __init__(self, driver):
        self.driver = driver

    add_to_cart = (By.ID, "add-to-cart-button")
    added_to_cart_message = (By.XPATH, "//span[contains(text(), 'Agregado al carrito')]")
    go_to_cart = (By.XPATH, "//*[@id='sw-gtc']//a[contains(text(),'Ir al carrito')]")

    def wait_until_add_to_cart_is_present(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*DetailProducts.add_to_cart]))

    def click_in_add_to_cart(self):
        self.driver.find_element(*DetailProducts.add_to_cart).click()

    def wait_until_message_added_to_cart(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*DetailProducts.added_to_cart_message]))

    def click_go_to_cart_button(self):
        self.driver.find_element(*DetailProducts.go_to_cart).click()
