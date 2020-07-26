from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
import pytest


# class TestSignInNegative:
#     @pytest.mark.parametrize(
#         "test_input,expected",
#         [
#             (
#                     {"email": "",
#                      "password": ""
#                      },
#                     "Bad email or password."
#             ),
#             (
#                     {"email": "mymail@i.ua",
#                      "password": "123456"
#                      },
#                     "Bad email or password.")
#         ]
#     )
#     def test_sign_in_error_message(
#             self,
#             browser_fixture,
#             test_input,
#             expected
#     ):
#         session_email = test_input["email"]
#         session_password = test_input["password"]
#         sign_in_page = SignInSearchHelper(browser_fixture)
#         common = CommonSearchHelper(browser_fixture)
#         sign_in_page.go_to_sign_in_page()
#         sign_in_page.type_sign_in_email(session_email)
#         sign_in_page.type_sign_in_password(session_password)
#         sign_in_page.click_sign_in_btn()
#         error_message = sign_in_page.error_message()
#         assert error_message == expected
#         assert session_email not in common.navbar_items()
#
#     @pytest.mark.parametrize(
#         "test_input,expected",
#         [
#             ({"email": "mymaili.ua", "password": "123456"}, "Bad email or password."),
#             ({"email": "mymaili@", "password": "123456"}, "Bad email or password.")
#         ]
#     )
#     def test_sign_in_tooltip(
#             self,
#             browser_fixture,
#             test_input,
#             expected
#     ):
#         session_email = test_input["email"]
#         session_password = test_input["password"]
#         sign_in_page = SignInSearchHelper(browser_fixture)
#         common = CommonSearchHelper(browser_fixture)
#         sign_in_page.go_to_sign_in_page()
#         sign_in_page.type_sign_in_email(session_email)
#         sign_in_page.type_sign_in_password(session_password)
#         sign_in_page.click_sign_in_btn()
#         assert session_email not in common.navbar_items()


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
                    "Bad email or password."
            ),
            (
                    {"email": "mymail@i.ua",
                     "password": "123456"
                     },
                    "Bad email or password.")
        ]
    )
    def test_error_all_required_fields_blank(
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
        common.click_addresses()

        addresses.click_on_element(
            AL.locator_new_address_link
        )

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
        breakpoint()
