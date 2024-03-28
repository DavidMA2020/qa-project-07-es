from selenium.webdriver.support.wait import WebDriverWait

import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage
import time
import UrbanRoutesFunctions

class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def create_controller(self):
        self.driver.get(data.urban_routes_url)
        self.driver.maximize_window()
        TestUrbanRoutes.routes_page = UrbanRoutesPage(self.driver)

    # Prueba 1: Configurar la dirección
    def test_set_route(self):
        self.create_controller()
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(TestUrbanRoutes.routes_page, 5)
        UrbanRoutesFunctions.function_set_route(address_from, address_to)
        WebDriverWait(self.driver, 3)
        assert UrbanRoutesPage.get_from(TestUrbanRoutes.routes_page) == address_from
        assert UrbanRoutesPage.get_to(TestUrbanRoutes.routes_page) == address_to
        time.sleep(2)


    # Prueba 2: Seleccionar la tarifa Comfort
    def test_select_tarif_conford(self):
        UrbanRoutesFunctions.function_select_tarif_conford()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)
        text_first_requirements = TestUrbanRoutes.routes_page.get_text_first_requirements()
        assert data.first_requirements_confort == text_first_requirements
        WebDriverWait(TestUrbanRoutes.routes_page, 3)


    # Prueba 3: Rellenar el número de teléfono (dentro de esta se recupera un codigo SMS)
    def test_register_phone_number(self):
        phone_number = data.phone_number
        UrbanRoutesFunctions.function_register_phone_number(phone_number)
        WebDriverWait(TestUrbanRoutes.routes_page, 3)
        text_div_phone_number = TestUrbanRoutes.routes_page.get_text_phone_number()
        assert phone_number == text_div_phone_number
        WebDriverWait(TestUrbanRoutes.routes_page, 3)


    # Prueba 4: Agregar una tarjeta de crédito (esto incluye el numero de tarjeta y el codigo CVV)
    def test_register_card(self):
        card_number = data.card_number
        card_code = data.card_code
        UrbanRoutesFunctions.function_register_card(card_number, card_code)
        WebDriverWait(TestUrbanRoutes.routes_page, 3)
        text_div_card = TestUrbanRoutes.routes_page.get_text_div_card()
        assert data.text_card == text_div_card
        TestUrbanRoutes.routes_page.click_close_payment_method()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)


    # Prueba 5: Escribir un mensaje para el controlador (Conductor del taxi)
    def test_message_for_driver(self):
        message_for_driver = data.message_for_driver
        UrbanRoutesFunctions.function_message_for_driver(message_for_driver)
        #WebDriverWait(TestUrbanRoutes.routes_page, 3)
        assert data.message_for_driver == TestUrbanRoutes.routes_page.get_message_for_driver()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 6: Pedir una manta y pañuelos
    def test_add_blanket_and_scarves(self):
        count_clics = 0
        new_count_clics = UrbanRoutesFunctions.function_add_blanket_and_scarves(count_clics)
        assert new_count_clics == 1
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 7: Pedir 2 helados
    def test_add_ice_cream(self):
        UrbanRoutesFunctions.function_add_ice_cream()
        count_ice_cream = TestUrbanRoutes.routes_page.get_count_ice_cream()
        assert data.total_ice_cream == count_ice_cream
        WebDriverWait(TestUrbanRoutes.routes_page, 3)


    # Prueba 8: Aparece el modal para buscar un taxi.
    def test_click_order_taxi(self):
        UrbanRoutesFunctions.function_click_order_taxi()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)
        assert TestUrbanRoutes.routes_page.get_text_form_searching_taxi()

    # Prueba 9: Esperar a que aparezca la información del conductor en el modal (opcional)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
