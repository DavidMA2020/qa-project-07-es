import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities

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

def get_phone_code(driver):
    respuesta = None
    for request in driver.requests:
        # Verificar si la solicitud es la que contiene la respuesta del servicio
        # Puedes hacer esto inspeccionando la URL de la solicitud u otros parámetros
        if "URL_del_servicio" in request.url:
            # Extraer la respuesta del cuerpo de la solicitud
            respuesta = request.response.body

    return respuesta

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    btn_take_taxi = (By.XPATH, ".//div[@class='results-text']/button[text()='Pedir un taxi']")
    btn_taxi_conford = (By.XPATH, ".//div[@class='tcard-icon']/img[@alt='Comfort']")
    btn_add_phone = (By.CLASS_NAME, 'np-button')
    number_phone_field = (By.ID, 'phone')
    btn_continue = (By.XPATH, ".//div[@class='buttons']/button[text()='Siguiente']") #(By.CLASS_NAME, 'buttons')
    validation_code_field = (By.XPATH, ".//div[@class='input-container']/input[@id='code']") # (By.ID, 'code')

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
    def wait_for_load_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(By.CLASS_NAME,'logo'))
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
    def register_number_phone(self, number_phone):
        self.click_add_phone_button()
        self.set_phone_number(number_phone)
        self.click_continue_add_phone_number_button()
        time.sleep(3)
        cod_sms = get_phone_code(self.driver)
        #ingresamos codigo de SMS
        self.set_cod_sms(cod_sms)
        time.sleep(3)
        #dar clic en el boton confirmar


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        #cls.driver = webdriver.Chrome() #agregado por DMA para pruebas
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        #self.driver.implicitly_wait(10)
        #routes_page.wait_for_load_page()  # agregamos tiempo de espera
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        time.sleep(5)
        #assert routes_page.get_from() == address_from
        #assert routes_page.get_to() == address_to
        routes_page.click_take_taxi_button()
        time.sleep(5)
        routes_page.click_taxi_confort_button()
        time.sleep(3)
        phone_number = data.phone_number
        routes_page.register_number_phone(phone_number)
        time.sleep(10)



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
