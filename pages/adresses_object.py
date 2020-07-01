from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressesLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_first_name_field = (By.NAME, "address[first_name]")


class AddressesSearchHelper(BasePage):
    def click_new_addresses_link(self):
        return self.find_element(
            AddressesLocators.locator_new_address_link, time=2).click()

    def first_name_field(self):
        return self.find_element(
            AddressesLocators.locator_first_name_field, time=2)