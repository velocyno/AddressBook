from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressesLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_first_name_field = (By.NAME, "address[first_name]")
    locator_last_name_field = (By.NAME, "address[last_name]")
    locator_address1_field = (By.NAME, "address[address1]")


class AddressesSearchHelper(BasePage):
    def click_new_addresses_link(self):
        return self.find_element(
            AddressesLocators.locator_new_address_link, time=2)\
            .click()

    def set_data_to_field(self, field_locator, data):
        return self.find_element(
            field_locator, time=2)\
            .send_keys(data)