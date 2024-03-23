import time
from main import TestUrbanRoutesEvidence
import data
def set_route():
    #self.create_controller()
    routes_page = TestUrbanRoutesEvidence.routes_page
    time.sleep(3) #WebDriverWait(driver, 3)
    address_from = data.address_from
    address_to = data.address_to
    routes_page.set_route(address_from, address_to)
    time.sleep(3)
    assert routes_page.get_from() == address_from
    assert routes_page.get_to() == address_to