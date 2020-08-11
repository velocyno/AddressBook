from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import Converters
import time
from tests.test_helper import TestHelper
import pytest


class TestEditAddressNegative:
    before_all = False

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
        if not TestEditAddressNegative.before_all:
            before_all = TestHelper()
            before_all.create_user(browser_fixture)
            before_all.add_address(browser_fixture, data_fixture_js)
            TestEditAddressNegative.before_all = True

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesSearchHelper(browser_fixture)

        addresses.click_on_element(AL.locator_edit_address_link)

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


        addresses.click_on_element(
            AL.locator_list_link
        )

