
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from retrieve_phone_code import retrieve_phone_code
import time

class UrbanRoutesPage:
    import selector

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.selector.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.selector.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.selector.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.selector.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def wait_for_load_selected_drive(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(self.selector.div_selected_drive))

    def get_text_form_searching_taxi(self):
        return self.driver.find_element(*self.selector.text_div_form_searching_taxi).text

    def click_take_taxi_button(self):
        self.driver.find_element(*self.selector.btn_take_taxi).click()

    def click_taxi_confort_button(self):
        self.driver.find_element(*self.selector.btn_taxi_conford).click()

    def click_add_phone_button(self):
        self.driver.find_element(*self.selector.btn_add_phone).click()

    def get_text_phone_number(self):
        return self.driver.find_element(*self.selector.btn_add_phone).text

    def get_text_div_card(self):
        return self.driver.find_element(*self.selector.div_text_card).text

    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.selector.number_phone_field).send_keys(number_phone)

    def click_continue_add_phone_number_button(self):
        self.driver.find_element(*self.selector.btn_continue).click()

    def set_cod_sms(self, cod_sms):
        self.driver.find_element(*self.selector.validation_code_field).send_keys(cod_sms)

    def click_confirm_add_phone_number_button(self):
        self.driver.find_element(*self.selector.btn_confirm).click()

    def register_number_phone(self, number_phone):
        self.click_add_phone_button()
        self.set_phone_number(number_phone)
        time.sleep(2)
        self.click_continue_add_phone_number_button()
        time.sleep(2)
        cod_sms = retrieve_phone_code(self.driver)
        self.set_cod_sms(cod_sms)
        time.sleep(2)
        self.click_confirm_add_phone_number_button()

    def get_text_first_requirements(self):
        return self.driver.find_element(*self.selector.div_first_requirements).text

    def click_add_payment_method_button(self):
        self.driver.find_element(*self.selector.btn_add_payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.selector.btn_add_card).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.selector.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.selector.card_code_field).send_keys(card_code)

    def click_div_img_card(self):
        self.driver.find_element(*self.selector.div_img_card).click()

    def click_save_card_button(self):
        self.driver.find_element(*self.selector.btn_save_card).click()

    def click_close_payment_method(self):
        self.driver.find_element(*self.selector.btn_close_payment_method).click()

    def register_payment_method(self, card_number, card_code):
        self.click_add_payment_method_button()
        time.sleep(3)
        self.click_add_card_button()
        time.sleep(2)
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        time.sleep(1)
        self.click_div_img_card()
        time.sleep(1)
        self.click_save_card_button()
        time.sleep(1)

    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.selector.message_for_driver_field).send_keys(message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.selector.message_for_driver_field).get_property('value')

    def click_add_blanket_and_scarves_button(self):
        self.driver.find_element(*self.selector.btn_add_blanket_and_scarves).click()

    def click_add_ice_cream_button(self):
        self.driver.find_element(*self.selector.btn_add_ice_cream).click()

    def get_count_ice_cream(self):
        return self.driver.find_element(*self.selector.div_count_ice_cream).text

    def click_order_taxi_button(self):
        self.driver.find_element(*self.selector.btn_order_taxi).click()
