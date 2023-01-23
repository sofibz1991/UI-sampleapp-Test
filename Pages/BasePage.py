from selenium.webdriver.common.by import By

class BasePage():
#funciones que comparten el resto de las paginas de la cual heredan  
    def __init__(self, driver):
        self.driver = driver 

    #METODOS

    def find_element_xpath(self,locator):
        return self.driver.find_element(By.XPATH, locator)

    def go_to_SampleApp(self,locator):
        element = self.find_element_xpath(locator)
        element.location_once_scrolled_into_view
        element.click()

    def do_send_keys(self,locator,value):
        element = self.find_element_xpath(locator)
        element.send_keys(value)

    def do_click(self,locator):
        element = self.find_element_xpath(locator)
        element.click()

    def get_element_text(self,locator):
        element = self.find_element_xpath(locator)
        text = element.text
        return text