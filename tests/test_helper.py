from selenium.common.exceptions import TimeoutException
from pages.sign_up_object import SignUpSearchHelper
from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.addresses_list_object import AddressesListLocators as ALL
from pages.new_address_object import NewAddressPage
from pages.new_address_object import NewAddressLocators as NAL
from pages.show_address_object import ShowAddressPage
from pages.new_address_object import Converters

# from pages.adresses_object import AddressesSearchHelper
# from pages.adresses_object import AddressesLocators as AL


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
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses_list_page = AddressesListPage(browser_fixture)
        new_address_page = NewAddressPage(browser_fixture)
        show_address_page = ShowAddressPage(browser_fixture)
        converter = Converters()

        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()

        addresses_list_page.click_on_element(
            ALL.locator_new_address_link
        )

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            data_fixture_js["dict_add_address"]["First name:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            data_fixture_js["dict_add_address"]["Last name:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            data_fixture_js["dict_add_address"]["Street Address:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_city,
            data_fixture_js["dict_add_address"]["City:"]
        )

        new_address_page.select_dropdown_option(
            NAL.locator_state,
            data_fixture_js["dict_add_address"]["State:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code,
            data_fixture_js["dict_add_address"]["Zip code:"]
        )

        new_address_page.select_state(
            data_fixture_js["dict_add_address"]["Country:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_birthday,
            converter.date_converter(
                data_fixture_js["dict_add_address"]["Birthday:"]
            )
        )

        new_address_page.set_data_to_field(
            NAL.locator_color,
            converter.rgb_to_hex(
                data_fixture_js["dict_add_address"]["Color:"]
            )
        )

        new_address_page.set_data_to_field(
            NAL.locator_age,
            data_fixture_js["dict_add_address"]["Age:"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_website,
            data_fixture_js["dict_add_address"]["Website:"]
        )

        new_address_page.find_element(NAL.locator_picture)\
            .send_keys("C:\\123.png")

        new_address_page.set_data_to_field(
            NAL.locator_phone,
            data_fixture_js["dict_add_address"]["Phone:"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_climbing,
            data_fixture_js["dict_add_address"]["Climbing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_dancing,
            data_fixture_js["dict_add_address"]["Dancing?"]
        )

        new_address_page.click_on_element_if_yes(
            NAL.locator_reading,
            data_fixture_js["dict_add_address"]["Reading?"]
        )

        new_address_page.set_data_to_field(
            NAL.locator_note,
            data_fixture_js["dict_add_address"]["Note:"]
        )

        new_address_page.click_on_element(
            NAL.locator_create_address_btn
        )

        common.click_sign_out()

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
