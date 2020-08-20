from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
import pytest


class TestAddAddressNegative:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                    {"first_name": "",
                     "last_name": "",
                     "address1": "",
                     "city": "",
                     "zip_code": ""
                     },
                    "5 errors prohibited this address from being saved:"
                    "\nFirst name can't be blank"
                    "\nLast name can't be blank"
                    "\nAddress1 can't be blank"
                    "\nCity can't be blank"
                    "\nZip code can't be blank"
            ),
            (
                    {"first_name": "Andrii",
                     "last_name": "",
                     "address1": "",
                     "city": "",
                     "zip_code": ""
                     },
                    "4 errors prohibited this address from being saved:"
                    "\nLast name can't be blank"
                    "\nAddress1 can't be blank"
                    "\nCity can't be blank"
                    "\nZip code can't be blank"
            ),
            (
                    {"first_name": "Andrii",
                     "last_name": "M",
                     "address1": "",
                     "city": "",
                     "zip_code": ""
                     },
                    "3 errors prohibited this address from being saved:"
                    "\nAddress1 can't be blank"
                    "\nCity can't be blank"
                    "\nZip code can't be blank"
            ),
            (
                    {"first_name": "Andrii",
                     "last_name": "M",
                     "address1": "Street",
                     "city": "",
                     "zip_code": ""
                     },
                    "2 errors prohibited this address from being saved:"
                    "\nCity can't be blank"
                    "\nZip code can't be blank"
            ),
            (
                    {"first_name": "Andrii",
                     "last_name": "M",
                     "address1": "Street",
                     "city": "Lviv",
                     "zip_code": ""
                     },
                    "1 error prohibited this address from being saved:"
                    "\nZip code can't be blank"
            ),
        ]
    )
    def test_error_required_fields_blank(
            self,
            browser_fixture,
            data_fixture_js,
            test_input,
            expected
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
            AL.locator_city,
            test_input["city"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            test_input["zip_code"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        error_message = common.get_text_from_element(
            AL.locator_required_fields_error
        )
        assert error_message == expected
        common.click_sign_out()
