from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = (By.NAME, "email")
    continue_button = (By.ID, "continue")
    password_input = (By.NAME, "password")
    sign_in_button = (By.ID, "signInSubmit")
    issue_message = (By.XPATH, "//*[contains(text(),'Se produjo un problema')] | //*[contains(text(),'Mensaje importante')] | //*[contains(text(),'Resuelve esta actividad para proteger tu cuenta')]")
    logotipo_amazon_return = (By.CSS_SELECTOR, "i[aria-label=Amazon]")

    def type_username(self, username):
        self.driver.find_element(*LoginPage.username_input).send_keys(str(username))
    def click_in_continue_button(self):
        self.driver.find_element(*LoginPage.continue_button).click()
    def type_password(self, password):
        self.driver.find_element(*LoginPage.password_input).send_keys(str(password))
    def click_in_sign_in_button(self):
        self.driver.find_element(*LoginPage.sign_in_button).click()
    def click_in_logotipo_amazon_return(self):
        self.driver.find_element(*LoginPage.logotipo_amazon_return).click()
    def wait_issue_message(self, seconds):
        WebDriverWait(self.driver, int(seconds)).until(expected_conditions.visibility_of_element_located([*LoginPage.issue_message]))