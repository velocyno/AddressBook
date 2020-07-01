from base.base_page import BasePage
from selenium.webdriver.common.by import By


class CommonLocators:
    # Header menu
    locator_navbar_menu = (By.ID, "navbar")
    locator_sign_out = (By.XPATH, '//*[@id="navbar"]/div[1]/a[3]')
    locator_addresses = (By.LINK_TEXT, "Addresses")


class CommonSearchHelper(BasePage):
    def navbar_items(self):
        return self.find_element(
            CommonLocators.locator_navbar_menu, time=2).text.split()

    def click_sign_out(self):
        return self.find_element(
            CommonLocators.locator_sign_out).click()

    def click_addresses(self):
        return self.find_element(
            CommonLocators.locator_addresses, time=2).click()
