from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CartShopping:

    def __init__(self, driver):
        self.driver = driver

    cart_title = (By.XPATH, "//h1[contains(text(),'Carrito')]")
    remove_product = (By.XPATH, "//input[@value='Eliminar']")
    empty_cart_message = (By.XPATH, "//*[contains(text(),'Tu carrito de Amazon está vacío')]")

    def wait_until_is_present_cart_title(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*CartShopping.cart_title]))

    def click_remove_product(self):
        self.driver.find_element(*CartShopping.remove_product).click()

    def wait_until_is_present_empty_cart_message(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(
            expected_conditions.visibility_of_element_located([*CartShopping.empty_cart_message]))

    def obtain_message_empty_cart(self):
        return self.driver.find_element(*CartShopping.empty_cart_message).text
