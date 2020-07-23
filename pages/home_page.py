from base.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePageLocators:
    locator_home_page_tittle = (By.CLASS_NAME, "text-center")


class HomePageSearchHelper(BasePage):
    def home_page_header(self):
        return self.find_element(
            HomePageLocators.locator_home_page_tittle,
            time=self.light_load_element
        ).text
