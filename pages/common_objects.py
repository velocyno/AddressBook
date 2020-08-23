from base.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.sign_in_object import SignInLocators
from pages.adresses_object import AddressesLocators


class NavbarLocators:
    locator_navbar_menu_items = (By.ID, "navbar")
    locator_sign_in_link = (By.ID, "sign-in")
    locator_sign_out_link = (By.XPATH, '//*[@id="navbar"]/div[1]/a[3]')
    locator_addresses_link = (By.LINK_TEXT, "Addresses")


class CommonSearchHelper(BasePage):
    def navbar_items(self):
        return self.find_element(
            NavbarLocators.locator_navbar_menu_items, time=2).text.split()

    def click_sign_in(self):
        return self.find_element(
            NavbarLocators.locator_sign_in_link).click()

    # def click_sign_out(self):
    #     return self.find_element(
    #         NavbarLocators.locator_sign_out_link, time=2).click()

    def click_sign_out(self):
        self.find_element(
            NavbarLocators.locator_sign_out_link, time=2).click()
        return self.find_element(SignInLocators.locator_sign_in_page_tittle)

    def click_addresses(self):
        self.find_element(
            NavbarLocators.locator_addresses_link, time=2).click()
        return self.find_element(AddressesLocators.locator_addresses_page_header)

    def get_text_from_element(self, locator):
        return self.find_element(locator, time=2).text
