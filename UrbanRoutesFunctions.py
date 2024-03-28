
from selenium.webdriver.support.wait import WebDriverWait
import data
import main
import time

def function_set_route(address_from,address_to):
    routes_page = main.TestUrbanRoutes.routes_page
    WebDriverWait(routes_page, 3)
    routes_page.set_route(address_from, address_to)
    WebDriverWait(routes_page, 3)

def function_select_tarif_conford():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_take_taxi_button()
    time.sleep(2)
    routes_page.click_taxi_confort_button()


def function_register_phone_number(phone_number):
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.register_number_phone(phone_number)
    WebDriverWait(routes_page, 3)


def function_register_card(card_number, card_code):
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.register_payment_method(card_number, card_code)


def function_message_for_driver(message_for_driver):
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.set_message_for_driver(message_for_driver)

def function_add_blanket_and_scarves(count_clics):
    routes_page = main.TestUrbanRoutes.routes_page
    #if count_clics == 0:
    routes_page.click_add_blanket_and_scarves_button()
    return count_clics + 1

def function_add_ice_cream():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_add_ice_cream_button()
    routes_page.click_add_ice_cream_button()
    WebDriverWait(routes_page, 3)


def function_click_order_taxi():
    routes_page = main.TestUrbanRoutes.routes_page
    routes_page.click_order_taxi_button()
    time.sleep(2)
