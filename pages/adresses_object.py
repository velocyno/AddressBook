from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddressesLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_first_name_field = (By.NAME, "address[first_name]")
    locator_last_name_field = (By.NAME, "address[last_name]")
    locator_address1_field = (By.NAME, "address[address1]")
    locator_address2_field = (By.NAME, "address[address2]")
    locator_city = (By.NAME, "address[city]")
    locator_state = (By.NAME, "address[state]")
    locator_zip_code = (By.NAME, "address[zip_code]")
    locator_address_country_us = (By.ID, "address_country_us")
    locator_address_country_canada = (By.ID, "address_country_canada")
    locator_birthday = (By.NAME, "address[birthday]")
    locator_color = (By.NAME, "address[color]")



class AddressesSearchHelper(BasePage):
    def click_new_addresses_link(self):
        return self.find_element(
            AddressesLocators.locator_new_address_link, time=2)\
            .click()

    def set_data_to_field(self, field_locator, data):
        return self.find_element(
            field_locator, time=2)\
            .send_keys(data)

    def select_state_dropdown(self, state):
        dropdown = Select(self.find_element(
            AddressesLocators.locator_state, time=2))
        return dropdown.select_by_visible_text(state)

    def select_radio_button(self, radio_locator):
        return self.find_element(radio_locator, time=2).click()
