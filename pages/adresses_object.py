from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddressesLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_show_list_link = (By.LINK_TEXT, "List")
    locator_edit_address_link = (By.LINK_TEXT, "Edit")
    locator_destroy_address_link = (By.LINK_TEXT, "Destroy")
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
    locator_age = (By.NAME, "address[age]")
    locator_website = (By.NAME, "address[website]")
    locator_picture = (By.ID, 'address_picture')
    locator_phone = (By.NAME, "address[phone]")
    locator_climbing = (By.ID, "address_interest_climb")
    locator_dancing = (By.ID, "address_interest_dance")
    locator_reading = (By.ID, "address_interest_read")
    locator_note = (By.ID, "address_note")
    locator_create_update_address_btn = (By.NAME, "commit")
    locator_result_container = (By.CLASS_NAME, "container")
    locator_container_options = (By.XPATH, "//p")
    # locator_container_options_key = (By.XPATH, ".//span[1]")
    # locator_container_options_value = (By.XPATH, ".//span[2]")


class AddressesSearchHelper(BasePage):
    def click_on_element(self, locator):
        return self.find_element(
            locator, time=2)\
            .click()

    def set_data_to_field(self, field_locator, data):
        return self.find_element(
            field_locator, time=2)\
            .send_keys(data)

    def select_dropdown_option(self, dropdown_locator, option):
        dropdown = Select(self.find_element(
            dropdown_locator, time=2))
        return dropdown.select_by_visible_text(option)

    def find_element_by_locator(self, locator):
        return self.find_element(locator, time=2)

    def find_elements_by_locator(self, locator, time=10):
        return self.find_elements(locator, time=2)

    def select_element_by_locator(self, locator):
        element = Select(self.find_element(locator, time=2))
        return element

