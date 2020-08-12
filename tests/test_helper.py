from selenium.common.exceptions import TimeoutException
from pages.sign_up_object import SignUpSearchHelper
from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import AddressesLocators as AL


class TestHelper:
    def create_user(self, browser_fixture):
        sign_up_page = SignUpSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.type_sign_up_email("mymail@i.ua")
        sign_up_page.type_sign_up_password("123456")
        sign_up_page.click_sign_up_btn()
        try:
            common.click_sign_out()
        except TimeoutException:
            pass

    def add_address(self, browser_fixture, data_fixture_js):
        session_email = "mymail@i.ua"
        session_password = "123456"

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
            data_fixture_js["dict_add_address"]["First name:"]
        )

        addresses.set_data_to_field(
            AL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"]
        )

        addresses.set_data_to_field(
            AL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"]
        )

        addresses.set_data_to_field(
            AL.locator_city,
            data_fixture_js["dict_add_address"]["City:"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            data_fixture_js["dict_add_address"]["Zip code:"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        addresses.click_on_element(
            AL.locator_list_link
        )

        # common.click_sign_out()

    # def add_address(self, browser_fixture, data_fixture_js):
    #     common = CommonSearchHelper(browser_fixture)
    #     addresses = AddressesSearchHelper(browser_fixture)
    #
    #     common.click_addresses()
    #
    #     addresses.click_on_element(
    #         AL.locator_new_address_link
    #     )
    #
    #     addresses.set_data_to_field(
    #         AL.locator_first_name_field,
    #         data_fixture_js["dict_add_address"]["First name:"]
    #     )
    #
    #     addresses.set_data_to_field(
    #         AL.locator_last_name_field,
    #         data_fixture_js["dict_add_address"]["Last name:"]
    #     )
    #
    #     addresses.set_data_to_field(
    #         AL.locator_address1_field,
    #         data_fixture_js["dict_add_address"]["Street Address:"]
    #     )
    #
    #     addresses.set_data_to_field(
    #         AL.locator_city,
    #         data_fixture_js["dict_add_address"]["City:"]
    #     )
    #
    #     addresses.set_data_to_field(
    #         AL.locator_zip_code,
    #         data_fixture_js["dict_add_address"]["Zip code:"]
    #     )
    #
    #     addresses.click_on_element(
    #         AL.locator_create_update_address_btn
    #     )
    #
    #     common.click_sign_out()
