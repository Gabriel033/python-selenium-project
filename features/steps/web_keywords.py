import datetime
import json

import allure
from allure_commons.types import AttachmentType
from behave import *
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from features.steps.browser import driver_context
from settings.conf import driver_options
from settings.pageObjects.HomePage import HomePage
from settings.pageObjects.LoginPage import LoginPage
from settings.pageObjects.SearchPage import SearchPage
from settings.pageObjects.DetailProducts import DetailProducts
from settings.pageObjects.CartShopping import CartShopping


####################################################################################
###########               Métodos Genéricos             ############################
####################################################################################
def obtain_parameters_element(element):

    # element = ["element.json", "AmazonSearchButton"]

    file_name = element.split("|:|")[0]
    # file_name = element.json
    element_name = element.split("|:|")[1]
    # element_name = AmazonSearchButton
    with open("./settings/input_data/" + file_name, 'r') as json_file:
        elements = json.load(json_file)
    for element in elements:
        if element == element_name:
            element_locator, element_by = elements[element_name]["loc"], get_by(elements[element_name]["find_by"])
    return str(element_locator), str(element_by)


def get_by(by):
    match by.upper():
        case "XPATH":
            return By.XPATH
        case "ID":
            return By.ID
        case "LINK_TEXT":
            return By.LINK_TEXT
        case "NAME":
            return By.NAME
        case "TAG_NAME":
            return By.TAG_NAME
        case "CLASS_NAME":
            return By.CLASS_NAME
        case "CSS_SELECTOR":
            return By.CSS_SELECTOR
        case "PARTIAL_LINK_TEXT":
            return By.PARTIAL_LINK_TEXT


def obtain_parameters_data(data):
    file_name = data.split("|:|")[0]
    data_name = data.split("|:|")[1]
    with open("./settings/input_data/" + file_name, 'r') as json_file:
        datas = json.load(json_file)
    for data in datas:
        if data == data_name:
            input_data = datas[data_name]
    return input_data


####################################################################################
###########                     Steps                   ############################
####################################################################################

@step(u'navigate to "{web}"')
def navigate_to_web(context, web):
    driver_context(context)
    if "|:|" in web:
        web = obtain_parameters_data(web)
    else:
        web = web
    context.driver.get(str(web))


@step(u'switch to frame with id "{id}"')
def switch_to_frame_with_id(context, id):
    context.driver.switch_to.frame(id)


@step(u'click on "{element}"')
def click_on(context, element):
    locator, find_by = obtain_parameters_element(element)
    context.driver.find_element(find_by, locator).click()


@step(u'select in the dropdown with xpath "{element}" the partial text "{value}"')
def select_in_dropdown_the_partial_text(context, element, value):
    locator, find_by = obtain_parameters_element(element)
    if "|:|" in value:
        value = obtain_parameters_data(value)
    else:
        value = value
    dropdown = context.driver.find_element(find_by, locator)
    dropdown.click()
    obj_dropdown_value = locator + "//following-sibling::*[contains(text(),'" + str(value) + "')]"
    partial_value = context.driver.find_element(find_by, obj_dropdown_value)
    partial_value.click()
    time.sleep(2)


@step(u'select from the dropdown "{element}" the index "{index}"')
def select_from_the_dropdown_the_index(context, element, index):
    locator, find_by = obtain_parameters_element(element)
    if "|:|" in index:
        index = obtain_parameters_data(index)
    else:
        index = index
    dropdown = Select(context.driver.find_element(find_by, locator))
    dropdown.select_by_index(int(index))


@step(u'select from the dropdown "{element}" the visible text "{text}"')
def select_from_dropdown_the_visible_text(context, element, text):
    locator, find_by = obtain_parameters_element(element)
    if "|:|" in text:
        text = obtain_parameters_data(text)
    else:
        text = text
    dropdown = Select(context.driver.find_element(find_by, locator))
    dropdown.select_by_visible_text(str(text))


@step(u'type on "{element}" the value "{value}"')
def type_on_element_the_value(context, element, value):
    locator, find_by = obtain_parameters_element(element)
    if "|:|" in value:
        value = obtain_parameters_data(value)
    else:
        value = value
    context.driver.find_element(find_by, locator).send_keys(value)


@step(u'clear the inputtext "{element}"')
def clear_the_inputtext(context, element):
    locator, find_by = obtain_parameters_element(element)
    context.driver.find_element(find_by, locator).clear()


@step(u'validate if element "{element}" is visible')
def validate_if_element_is_visible(context, element):
    locator, find_by = obtain_parameters_element(element)
    element = context.driver.find_element(find_by, locator)
    if element.is_displayed():
        pass
    else:
        raise Exception("Element not visible, it is not expected")


@step(u'validate if element "{element}" is not visible')
def validate_if_element_is_not_visible(context, element):
    locator, find_by = obtain_parameters_element(element)
    element = context.driver.find_element(find_by, locator)
    if element.is_displayed():
        raise Exception("Element is visible, but it is not expected")
    else:
        pass


@step(u'the element "{element}" should contain the text "{text}"')
def the_element_must_contain_the_text(context, element, text):
    locator, find_by = obtain_parameters_element(element)
    element = context.driver.find_element(find_by, locator)
    if "|:|" in text:
        text = obtain_parameters_data(text)
    else:
        text = text

    if text in element.text:
        pass
    else:
        raise Exception("The element not contains the text expected")


@step(u'click on dynamic element with the text "{text}"')
def click_on_dynamic_element_with_the_text(context, text):
    if "|:|" in text:
        text = obtain_parameters_data(text)
    else:
        text = text
    element = context.driver.find_element(By.XPATH, "//*[contains(text(),'" + str(text) + "')] | //*[text()='" + str(text) + "']")
    element.click()


@step(u'click on button "{element}" and accept alert if it is present')
def click_on_button_and_accept_alrt_if_it_is_present(context, element):
    locator, find_by = obtain_parameters_element(element)
    context.driver.find_element(find_by, locator).click()
    try:
        Alert(context.driver).accept()
    except:
        pass


@step(u'accept alert')
def accept_alert(context):
    Alert(context.driver).accept()


@step(u'cancel alert')
def cancel_alert(context):
    Alert(context.driver).dismiss()


@step(u'press the key "{key}"')
def press_key(context, key):
    actions = ActionChains(context.driver)
    try:
        key = getattr(Keys, key.upper())
    except:
        raise Exception("That key is not available")
    actions.send_keys(key).perform()


@step(u'open new window')
def open_new_window(context):
    context.driver.execute_script("window.open('');")


@step(u'switch to window tab number "{number}"')
def switch_to_window_tab_number(context, number):
    context.driver.switch_to.window(context.driver.window_handles[int(number)])


@step(u'switch to previous window')
def switch_to_previous_window(context):
    current_window = context.driver.current_window_handle
    all_guid = context.driver.window_handles
    num_of_handles = len(all_guid)
    for num in range(num_of_handles):
        if all_guid[num] == current_window:
            window_selected = all_guid[num - 1]
            context.driver.switch_to.window(window_selected)
            break


@step(u'switch to new window opened previously')
def switch_to_new_window_opened_previously(context):
    current_window = context.driver.current_window_handle
    all_guid = context.driver.window_handles
    num_of_handles = len(all_guid)
    for num in range(num_of_handles):
        if all_guid[num] == current_window:
            window_selected = all_guid[num + 1]
            context.driver.switch_to.window(window_selected)
            break


@step(u'upload file "{path}" in the element "{element}"')
def upload_file_from_with_name_in_element(context, path, element):
    locator, find_by = obtain_parameters_element(element)
    if "|:|" in path:
        path = obtain_parameters_data(path)
    else:
        path = path

    context.driver.find_element(find_by, locator).send_keys(path)


@step(u'wait for "{seconds}" seconds')
def wait_time_seconds(context, seconds):
    time.sleep(int(seconds))


@step(u'wait until "{element}" is visible in a maximum of "{seconds}" seconds')
def wait_until_element_is_visible_in_a_maximum_of_time(context, element, seconds):
    #max_time = driver_options.EXECUTION_OPTIONS.get('explicity-wait')
    locator, find_by = obtain_parameters_element(element)
    WebDriverWait(context.driver, int(seconds)).until(
        expected_conditions.presence_of_element_located((find_by, locator)))


@step(u'take screenshot')
def take_screenshot(context):
    time_now = datetime.datetime.now()
    date_now = (str(time_now.day) + "_" + str(time_now.month) + "_" + str(time_now.year) + " " + str(time_now.hour) +
                "_" + str(time_now.minute) + "_" + str(time_now.second))
    allure.attach(context.driver.get_screenshot_as_png(), name="take_screenshot_"+date_now,
                  attachment_type=AttachmentType.PNG)

@step(u'close browser')
def close_browser(context):
    context.driver.close()

@step(u'do login in the Amazon page with user "{user}" and password "{password}"')
def do_login_in_amazon(context, user, password):
    if "|:|" in user:
        user = obtain_parameters_data(user)
    else:
        user = user
    if "|:|" in password:
        password = obtain_parameters_data(password)
    else:
        password = password

    # Declaración inicial de objetos de las páginas
    home_page = HomePage(context.driver)
    login_page = LoginPage(context.driver)

    # Acceso a página de login
    home_page.move_to_MenuCuentas()
    take_screenshot(context)
    home_page.click_in_dentificarse_button()

    # Intento para hacer login
    login_page.type_username(user)
    take_screenshot(context)
    login_page.click_in_continue_button()
    login_page.type_password(password)
    take_screenshot(context)
    login_page.click_in_sign_in_button()
    login_page.wait_issue_message(20)
    take_screenshot(context)

@step(u'return to the main page of amazon')
def return_main_page_amazon(context):
    login_page = LoginPage(context.driver)
    home_page = HomePage(context.driver)

    # Regresar a la página principal
    login_page.click_in_logotipo_amazon_return()
    # Esperar a que cargue la página
    home_page.wait_until_logo_amazon_is_present(30)
    # Tomar evidencia
    take_screenshot(context)

@step(u'search the product "{product}" and add it to the shopping cart')
def search_product_and_add_it_to_shopping_cart(context, product):
    if "|:|" in product:
        product = obtain_parameters_data(product)
    else:
        product = product

    # Declaración inicial de objetos de las páginas
    home_page = HomePage(context.driver)
    search_page = SearchPage(context.driver)
    product_details = DetailProducts(context.driver)

    # Escribir qué producto vamos a buscar
    home_page.type_product_search(product)
    # Tomar evidencia
    take_screenshot(context)
    # Dar click en el botón de buscar
    home_page.click_product_search()

    # Esperar hasta que aparezca el título de resultados
    search_page.wait_until_result_is_present(30)
    time.sleep(5)
    # Tomar evidencia
    take_screenshot(context)
    # Seleccionar primera opción de producto
    search_page.select_first_product()

    # Esperar hasta que aparezca los detalles del producto seleccionado
    product_details.wait_until_add_to_cart_is_present(30)
    # Tomar evidencia
    take_screenshot(context)
    # Agregar el producto al carrito de compra
    product_details.click_in_add_to_cart()

@step(u'the shopping cart should contains the product selected')
def the_shoppint_cart_should_contains_the_product(context):
    # Declaración inicial de clases
    product_details = DetailProducts(context.driver)
    cart_shopping = CartShopping(context.driver)

    # Esperar hasta que aparezca que se haya agregado el producto al carrito de compra
    product_details.wait_until_message_added_to_cart(30)
    # Tomar evidencia
    take_screenshot(context)
    # Dar click en ir a carrito de compras
    product_details.click_go_to_cart_button()
    # Esperar el título de carrito de compras
    cart_shopping.wait_until_is_present_cart_title(30)
    # Tomar evidencia
    take_screenshot(context)

@step(u'it is being removed the product in the shopping cart')
def it_is_being_removed_the_product(context):
    cart_shopping = CartShopping(context.driver)
    # Dar click en remover producto
    cart_shopping.click_remove_product()

@step(u'the shopping cart must be empty with the message "{message}"')
def the_shopping_cart_must_be_empty_with_the_message(context, message):
    cart_shopping = CartShopping(context.driver)

    # Esperar mensaje de carrito vacío
    cart_shopping.wait_until_is_present_empty_cart_message(30)
    # Tomar evidencia
    take_screenshot(context)
    # Assertion de mensaje
    assert(message in cart_shopping.obtain_message_empty_cart())
