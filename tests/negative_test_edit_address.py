from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import Converters
import time
from tests.test_helper import TestHelper
import pytest


class TestEditAddressNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                    {
                        "first_name": "",
                        "last_name": "Marm",
                        "address1": "Street",
                        "city": "Lviv",
                        "zip_code": "79000"
                    },
                    "1 error prohibited this address from being saved:"
                    "\nFirst name can't be blank"
            ),
            (
                    {
                        "first_name": "Andrii",
                        "last_name": "",
                        "address1": "Street",
                        "city": "Lviv",
                        "zip_code": "79000"
                    },
                    "1 error prohibited this address from being saved:"
                    "\nLast name can't be blank"
            ),
            (
                    {
                        "first_name": "Andrii",
                        "last_name": "Marm",
                        "address1": "",
                        "city": "Lviv",
                        "zip_code": "79000"
                    },
                    "1 error prohibited this address from being saved:"
                    "\nAddress1 can't be blank"
            ),
            (
                    {
                        "first_name": "Andrii",
                        "last_name": "Marm",
                        "address1": "",
                        "city": "Lviv",
                        "zip_code": "79000"
                    },
                    "1 error prohibited this address from being saved:"
                    "\nAddress1 can't be blank"
            ),
            (
                    {
                        "first_name": "Andrii",
                        "last_name": "Marm",
                        "address1": "Street",
                        "city": "",
                        "zip_code": "79000"
                    },
                    "1 error prohibited this address from being saved:"
                    "\nCity can't be blank"
            ),
            (
                    {
                        "first_name": "Andrii",
                        "last_name": "Marm",
                        "address1": "Street",
                        "city": "Lviv",
                        "zip_code": ""
                    },
                    "1 error prohibited this address from being saved:"
                    "\nZip code can't be blank"
            )
        ]
    )
    def test_edit_address_negative(
            self,
            browser_fixture,
            data_fixture_js,
            test_input,
            expected
    ):
        session_email = data_fixture_js["session_email"]
        session_password = data_fixture_js["session_password"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesSearchHelper(browser_fixture)
        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()

        test_helper = TestHelper()
        test_helper.add_address(browser_fixture, data_fixture_js)

        addresses.clean_field(AL.locator_first_name_field)
        addresses.clean_field(AL.locator_last_name_field)
        addresses.clean_field(AL.locator_address1_field)
        addresses.clean_field(AL.locator_city)
        addresses.clean_field(AL.locator_zip_code)

        addresses.set_data_to_field(
            AL.locator_first_name_field,
            test_input["first_name"]
        )

        addresses.set_data_to_field(
            AL.locator_last_name_field,
            test_input["last_name"]
        )

        addresses.set_data_to_field(
            AL.locator_address1_field,
            test_input["address1"]
        )

        addresses.set_data_to_field(
            AL.locator_address2_field,
            test_input["city"]
        )

        addresses.set_data_to_field(
            AL.locator_address2_field,
            test_input["zip_code"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        error_message = common.get_text_from_element(
            AL.locator_required_fields_error
        )

        assert error_message == expected
