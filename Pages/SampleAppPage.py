import time
from Pages.BasePage import BasePage
from config.config import TestData
from config.locators import Locators
#metodos para interacuar especificamente con text input page

class SampleAppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def go_to_SampleApp2(self):
        self.go_to_SampleApp(Locators.acceso_SampleApp)
        time.sleep(4)

    def do_exercise(self,uservalue, passwordvalue):
        self.do_send_keys(Locators.usuario_input,uservalue)
        self.do_send_keys(Locators.psw_input,passwordvalue)
        self.do_click(Locators.boton)
        banner_text = self.get_element_text(Locators.banner)
        return banner_text