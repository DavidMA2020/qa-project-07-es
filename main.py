import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    btn_take_taxi = (By.XPATH, ".//div[@class='results-text']/button[text()='Pedir un taxi']")
    btn_taxi_conford = (By.XPATH, ".//div[@class='tcard-icon']/img[@alt='Comfort']")
    btn_add_phone = (By.CLASS_NAME, 'np-button')
    number_phone_field = (By.ID, 'phone')
    btn_continue = (By.XPATH, ".//div[@class='buttons']/button[text()='Siguiente']")
    validation_code_field = (By.XPATH, ".//div[@class='input-container']/input[@id='code']")
    btn_confirm = (By.XPATH, ".//div[@class='buttons']/button[text()='Confirmar']")
    btn_add_payment_method = (By.XPATH, ".//div[@class='pp-value-container']/img[@alt='cash']")
    btn_add_card = (By.XPATH, ".//div[@class='pp-plus-container']/img[@alt='plus']")
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, ".//div[@class='card-code-input']/input[@id='code']")
    div_img_card = (By.XPATH, ".//div[@class='card-second-row']/div[@class='plc']")
    btn_save_card = (By.XPATH, ".//div[@class='pp-buttons']/button[text()='Agregar']")
    btn_close_payment_method = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/button")
    message_for_driver_field = (By.ID, 'comment')
    btn_add_blanket_and_scarves = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    btn_add_ice_cream = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    btn_order_taxi = (By.XPATH, "/html/body/div/div/div[3]/div[4]/button")
    div_selected_drive = (By.XPATH, "/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def wait_for_load_selected_drive(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(self.div_selected_drive))

    def click_take_taxi_button(self):
        self.driver.find_element(*self.btn_take_taxi).click()

    def click_taxi_confort_button(self):
        self.driver.find_element(*self.btn_taxi_conford).click()

    def click_add_phone_button(self):
        self.driver.find_element(*self.btn_add_phone).click()

    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.number_phone_field).send_keys(number_phone)

    def click_continue_add_phone_number_button(self):
        self.driver.find_element(*self.btn_continue).click()

    def set_cod_sms(self, cod_sms):
        self.driver.find_element(*self.validation_code_field).send_keys(cod_sms)

    def click_confirm_add_phone_number_button(self):
        self.driver.find_element(*self.btn_confirm).click()

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

    def click_add_payment_method_button(self):
        self.driver.find_element(*self.btn_add_payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.btn_add_card).click()

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def click_div_img_card(self):
        self.driver.find_element(*self.div_img_card).click()

    def click_save_card_button(self):
        self.driver.find_element(*self.btn_save_card).click()

    def click_close_payment_method(self):
        self.driver.find_element(*self.btn_close_payment_method).click()

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
        self.click_close_payment_method()
        time.sleep(1)

    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.message_for_driver_field).send_keys(message_for_driver)

    def click_add_blanket_and_scarves_button(self):
        self.driver.find_element(*self.btn_add_blanket_and_scarves).click()

    def click_add_ice_cream_button(self):
        self.driver.find_element(*self.btn_add_ice_cream).click()

    def click_order_taxi_button(self):
        self.driver.find_element(*self.btn_order_taxi).click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        self.driver.maximize_window()
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        time.sleep(3)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.click_take_taxi_button()
        time.sleep(2)
        routes_page.click_taxi_confort_button()
        time.sleep(3)
        phone_number = data.phone_number
        routes_page.register_number_phone(phone_number)
        time.sleep(2)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.register_payment_method(card_number, card_code)
        time.sleep(2)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        time.sleep(2)
        routes_page.click_add_blanket_and_scarves_button()
        time.sleep(2)
        routes_page.click_add_ice_cream_button()
        routes_page.click_add_ice_cream_button()
        time.sleep(2)
        routes_page.click_order_taxi_button()
        time.sleep(40)
        routes_page.wait_for_load_selected_drive()
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
