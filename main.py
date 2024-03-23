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
        WebDriverWait(TestUrbanRoutes.routes_page, 3)
        UrbanRoutesFunctions.function_set_route()
        time.sleep(2)

    # Prueba 2: Seleccionar la tarifa Comfort
    def test_select_tarif_conford(self):
        UrbanRoutesFunctions.function_select_tarif_conford()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 3: Rellenar el número de teléfono (dentro de esta se recupera un codigo SMS)
    def test_register_phone_number(self):
        UrbanRoutesFunctions.function_register_phone_number()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

        # Prueba 4: Agregar una tarjeta de crédito (esto incluye el numero de tarjeta y el codigo CVV)
    def test_register_card(self):
        UrbanRoutesFunctions.function_register_card()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 5: Escribir un mensaje para el controlador (Conductor del taxi)
    def test_message_for_driver(self):
        UrbanRoutesFunctions.function_message_for_driver()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 6: Pedir una manta y pañuelos
    def test_add_blanket_and_scarves(self):
        UrbanRoutesFunctions.function_add_blanket_and_scarves()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 7: Pedir 2 helados
    def test_add_ice_cream(self):
        UrbanRoutesFunctions.function_add_ice_cream()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 8: Aparece el modal para buscar un taxi.
    def test_click_order_taxi(self):
        UrbanRoutesFunctions.function_click_order_taxi()
        WebDriverWait(TestUrbanRoutes.routes_page, 3)

    # Prueba 9: Esperar a que aparezca la información del conductor en el modal (opcional)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
