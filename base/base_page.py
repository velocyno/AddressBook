from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost:3000/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time)\
            .until(EC.presence_of_element_located(locator),
                   message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time)\
            .until(EC.presence_of_all_elements_located(locator),
                   message=f"Can't find elements by locator {locator}")

    def click_on_element(self, locator):
        return self.find_element(locator).click()

    def go_to_home_page(self):
        return self.driver.get(self.base_url)

    def go_to_sign_up_page(self):
        return self.driver.get(self.base_url + "sign_up")

    def go_to_sign_in_page(self):
        return self.driver.get(self.base_url + "sign_in")
