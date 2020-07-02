from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import (AddressesLocators as AL,
                                   AddressesSearchHelper)


def test_add_address(browser_fixture):
    session_email = "andrii1@i.ua"
    session_password = "123456"
    page = SignInSearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)  # is it correct
    addresses = AddressesSearchHelper(browser_fixture)
    page.go_to_sign_in_page()
    page.type_sign_in_email(session_email)
    page.type_sign_in_password(session_password)
    page.click_sign_in_btn()
    common.click_addresses()
    addresses.click_new_addresses_link()
    addresses.set_data_to_field(AL.locator_first_name_field, "Andrii")
    addresses.set_data_to_field(AL.locator_last_name_field, "AQA")
    addresses.set_data_to_field(AL.locator_address1_field, "Street")
    addresses.set_data_to_field(AL.locator_address2_field, "Street2")
    addresses.set_data_to_field(AL.locator_city, "Lviv")
    addresses.select_state_dropdown("Alaska")
    addresses.set_data_to_field(AL.locator_zip_code, "79000")
    addresses.select_radio_button(AL.locator_address_country_us)
    addresses.set_data_to_field(AL.locator_birthday, "11.06.1985")
    addresses.set_data_to_field(AL.locator_color, "#00FF33")
    breakpoint()
