import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from settings.conf import driver_options


def options_selected(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise Exception("The browser that you have selected was not integrated to this project")

    if driver_options.DRIVER_CONFIG.get('start-maximized', False):
        options.add_argument("--start-maximized")
    if driver_options.DRIVER_CONFIG.get('headless', False):
        options.add_argument("headless")
    if driver_options.DRIVER_CONFIG.get('ignore-certificate-errors', False):
        options.add_argument("--ignore-certificate-errors")
    options.add_argument("window-size=" + str(driver_options.DRIVER_CONFIG.get('window-size')))
    if driver_options.DRIVER_CONFIG.get('ignore-certificate-errors', False):
        options.add_argument("--no-sandbox")
    if driver_options.DRIVER_CONFIG.get('disable-popup-blocking', False):
        options.add_argument("--disable-popup-blocking")
    return options


def driver_context(context):
    if context.driver is None:
        browser = driver_options.DRIVER_CONFIG.get('driver_type')
        if browser.lower() == "firefox":
            capabilities = options_selected(browser.lower())
            service_obj = Service("./settings/drivers/geckodriver.exe")
            context.driver = webdriver.Firefox(service=service_obj, options=capabilities)
        elif browser.lower() == "edge":
            capabilities = options_selected(browser.lower())
            service_obj = Service("./settings/drivers/msedgedriver.exe")
            context.driver = webdriver.Edge(service=service_obj, options=capabilities)
        elif browser.lower() == "chrome":
            capabilities = options_selected(browser.lower())
            service_obj = Service("./settings/drivers/chromedriver.exe")
            context.driver = webdriver.Chrome(service=service_obj, options=capabilities)
        else:
            raise Exception("Driver selected is not available")
        context.driver.implicitly_wait(int(driver_options.EXECUTION_OPTIONS.get('implicitly-wait')))
