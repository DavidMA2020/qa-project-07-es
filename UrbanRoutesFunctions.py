
from selenium.webdriver.support.wait import WebDriverWait
import data
import main
import time

def function_set_route():
    routes_page = main.TestUrbanRoutes.routes_page
    WebDriverWait(routes_page, 3)
    address_from = data.address_from
    address_to = data.address_to
    routes_page.set_route(address_from, address_to)
    WebDriverWait(routes_page, 3)
    assert routes_page.get_from() == address_from
    assert routes_page.get_to() == address_to

def function_select_tarif_conford():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_take_taxi_button()
    time.sleep(2)
    routes_page.click_taxi_confort_button()
    WebDriverWait(routes_page, 3)
    text_first_requirements = routes_page.get_text_first_requirements()
    assert data.first_requirements_confort == text_first_requirements

def function_register_phone_number():
    routes_page = main.TestUrbanRoutes.routes_page
    phone_number = data.phone_number
    routes_page.register_number_phone(phone_number)
    WebDriverWait(routes_page, 3)
    text_div_phone_number = routes_page.get_text_phone_number()
    assert data.phone_number == text_div_phone_number

def function_register_card():
    routes_page = main.TestUrbanRoutes.routes_page
    card_number = data.card_number
    card_code = data.card_code
    routes_page.register_payment_method(card_number, card_code)
    text_div_card = routes_page.get_text_div_card()
    assert data.text_card == text_div_card
    routes_page.click_close_payment_method()

def function_message_for_driver():
    routes_page = main.TestUrbanRoutes.routes_page
    message_for_driver = data.message_for_driver
    routes_page.set_message_for_driver(message_for_driver)
    assert data.message_for_driver == routes_page.get_message_for_driver()

def function_add_blanket_and_scarves():
    routes_page = main.TestUrbanRoutes.routes_page
    count_clics = 0
    if count_clics == 0:
        routes_page.click_add_blanket_and_scarves_button()
        count_clics = count_clics + 1
    else:
        count_clics = 0
    assert  count_clics == 1

def function_add_ice_cream():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_add_ice_cream_button()
    routes_page.click_add_ice_cream_button()
    WebDriverWait(routes_page, 3)
    count_ice_cream = routes_page.get_count_ice_cream()
    assert data.total_ice_cream == count_ice_cream

def function_click_order_taxi():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_order_taxi_button()
    WebDriverWait(routes_page, 3)
    assert routes_page.get_text_form_searching_taxi()