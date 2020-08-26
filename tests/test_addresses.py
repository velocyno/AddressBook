from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import Converters
import time


class TestManageAddresses:
    def test_add_address(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email2"]
        session_password = data_fixture_js["session_password2"]

        page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses = AddressesSearchHelper(browser_fixture)
        converter = Converters()

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
            AL.locator_address2_field,
            data_fixture_js["dict_add_address"]["Secondary Address:"]
        )

        addresses.set_data_to_field(
            AL.locator_city,
            data_fixture_js["dict_add_address"]["City:"]
        )

        addresses.select_dropdown_option(
            AL.locator_state,
            data_fixture_js["dict_add_address"]["State:"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            data_fixture_js["dict_add_address"]["Zip code:"]
        )

        addresses.select_state(
            data_fixture_js["dict_add_address"]["Country:"]
        )

        addresses.set_data_to_field(
            AL.locator_birthday,
            converter.date_converter(
                data_fixture_js["dict_add_address"]["Birthday:"]
            )
        )

        addresses.set_data_to_field(
            AL.locator_color,
            converter.rgb_to_hex(
                data_fixture_js["dict_add_address"]["Color:"]
            )
        )

        addresses.set_data_to_field(
            AL.locator_age,
            data_fixture_js["dict_add_address"]["Age:"]
        )

        addresses.set_data_to_field(
            AL.locator_website,
            data_fixture_js["dict_add_address"]["Website:"]
        )

        addresses.find_element(AL.locator_picture)\
            .send_keys("C:\\123.png")

        addresses.set_data_to_field(
            AL.locator_phone,
            data_fixture_js["dict_add_address"]["Phone:"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_climbing,
            data_fixture_js["dict_add_address"]["Climbing?"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_dancing,
            data_fixture_js["dict_add_address"]["Dancing?"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_reading,
            data_fixture_js["dict_add_address"]["Reading?"]
        )

        addresses.set_data_to_field(
            AL.locator_note,
            data_fixture_js["dict_add_address"]["Note:"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        dict_results = {}

        results = addresses.find_elements(
            AL.locator_container_options
        )

        for element in results:
            key = element.find_element_by_xpath('.//span[1]').text
            value = element.find_element_by_xpath('.//span[2]').text
            if key == 'Color:':
                value = element.find_element_by_xpath('.//span[2]')
                value = value.get_attribute('style').split("rgb")[1].rstrip(";")
            dict_results[key] = value
        assert addresses.find_element(
            AL.locator_result_container).text.split('\n')[0]\
               == "Address was successfully created."
        assert data_fixture_js["dict_add_address"] == dict_results
        addresses.click_on_element(AL.locator_list_link)

    def test_show_address(self, browser_fixture, data_fixture_js):
        addresses = AddressesSearchHelper(browser_fixture)
        time.sleep(2)
        addresses.click_on_element(
            AL.locator_show_address_link
        )
        time.sleep(2)
        dict_results = {}
        results = addresses.find_elements(
            AL.locator_container_options
        )
        for element in results:
            key = element.find_element_by_xpath('.//span[1]').text
            value = element.find_element_by_xpath('.//span[2]').text
            if key == 'Color:':
                value = element.find_element_by_xpath('.//span[2]')
                value = value.get_attribute('style').split("rgb")[1].rstrip(";")
            dict_results[key] = value
            pass
        assert data_fixture_js["dict_add_address"] == dict_results
        addresses.click_on_element(AL.locator_list_link)
        time.sleep(2)

    def test_edit_addresses(self, browser_fixture, data_fixture_js):
        addresses = AddressesSearchHelper(browser_fixture)

        addresses.click_on_element(
            AL.locator_edit_address_link
        )

        converter = Converters()

        addresses.clean_field(AL.locator_first_name_field)
        addresses.clean_field(AL.locator_last_name_field)
        addresses.clean_field(AL.locator_address1_field)
        addresses.clean_field(AL.locator_address2_field)
        addresses.clean_field(AL.locator_city)
        addresses.clean_field(AL.locator_zip_code)
        addresses.clean_field(AL.locator_age)
        addresses.clean_field(AL.locator_website)
        addresses.clean_field(AL.locator_phone)
        addresses.clean_field(AL.locator_note)

        addresses.set_data_to_field(
            AL.locator_first_name_field,
            data_fixture_js["dict_edit_address"]["First name:"]
        )

        addresses.set_data_to_field(
            AL.locator_last_name_field,
            data_fixture_js["dict_edit_address"]["Last name:"]
        )

        addresses.set_data_to_field(
            AL.locator_address1_field,
            data_fixture_js["dict_edit_address"]["Street Address:"]
        )

        addresses.set_data_to_field(
            AL.locator_address2_field,
            data_fixture_js["dict_edit_address"]["Secondary Address:"]
        )

        addresses.set_data_to_field(
            AL.locator_city,
            data_fixture_js["dict_edit_address"]["City:"]
        )

        addresses.select_dropdown_option(
            AL.locator_state,
            data_fixture_js["dict_edit_address"]["State:"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            data_fixture_js["dict_edit_address"]["Zip code:"]
        )

        addresses.select_state(
            data_fixture_js["dict_edit_address"]["Country:"]
        )

        addresses.set_data_to_field(
            AL.locator_birthday,
            converter.date_converter(
                data_fixture_js["dict_edit_address"]["Birthday:"]
            )
        )

        addresses.set_data_to_field(
            AL.locator_color,
            converter.rgb_to_hex(
                data_fixture_js["dict_edit_address"]["Color:"]
            )
        )

        addresses.set_data_to_field(
            AL.locator_age,
            data_fixture_js["dict_edit_address"]["Age:"]
        )

        addresses.set_data_to_field(
            AL.locator_website,
            data_fixture_js["dict_edit_address"]["Website:"]
        )

        # addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")

        addresses.set_data_to_field(
            AL.locator_phone,
            data_fixture_js["dict_edit_address"]["Phone:"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_climbing,
            data_fixture_js["dict_edit_address"]["Climbing?"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_dancing,
            data_fixture_js["dict_edit_address"]["Dancing?"]
        )

        addresses.click_on_element_if_yes(
            AL.locator_reading,
            data_fixture_js["dict_edit_address"]["Reading?"]
        )

        addresses.set_data_to_field(
            AL.locator_note,
            data_fixture_js["dict_edit_address"]["Note:"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        dict_results = {}
        results = addresses.find_elements(
            AL.locator_container_options
        )
        for element in results:
            key = element.find_element_by_xpath('.//span[1]').text
            value = element.find_element_by_xpath('.//span[2]').text
            if key == 'Color:':
                value = element.find_element_by_xpath('.//span[2]')
                value = value.get_attribute('style').split("rgb")[1].rstrip(";")
            dict_results[key] = value
        assert addresses.find_element(
            AL.locator_result_container).text.split('\n')[0] \
               == "Address was successfully updated."
        assert data_fixture_js["dict_edit_address"] == dict_results
        addresses.click_on_element(AL.locator_list_link)

    def test_destroy_address(self, browser_fixture):
        addresses = AddressesSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        addresses.click_on_element(AL.locator_destroy_address_link)
        popup = addresses.driver.switch_to.alert
        popup.accept()
        time.sleep(2)
        assert addresses.find_element(
            AL.locator_destroyed_message).text == "Address was successfully destroyed."
        common.click_sign_out()
