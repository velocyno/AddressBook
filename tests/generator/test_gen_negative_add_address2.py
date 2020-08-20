from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
import json
import pytest


class TestAddAddressNegative:

    def test_error_required_fields_blank(
            self,
            browser_fixture,
            data_fixture_js,
            data_gen
    ):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]
        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesSearchHelper(browser_fixture)
        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses.click_on_element(
            AL.locator_new_address_link
        )

        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesSearchHelper(browser_fixture)

        addresses.set_data_to_field(
            AL.locator_first_name_field,
            data_gen['test_input']['first_name']
        )

        addresses.set_data_to_field(
            AL.locator_last_name_field,
            data_gen['test_input']["last_name"]
        )

        addresses.set_data_to_field(
            AL.locator_address1_field,
            data_gen['test_input']["address1"]
        )

        addresses.set_data_to_field(
            AL.locator_city,
            data_gen['test_input']["city"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            data_gen['test_input']["zip_code"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        error_message = common.get_text_from_element(
            AL.locator_required_fields_error
        )
        assert error_message == data_gen["expected"]
        common.click_sign_out()
