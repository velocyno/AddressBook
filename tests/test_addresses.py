from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
import time


def test_add_address(browser_fixture):
    session_email = "andrii1@i.ua"
    session_password = "123456"
    page = SignInSearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)
    addresses = AddressesSearchHelper(browser_fixture)
    page.go_to_sign_in_page()
    page.type_sign_in_email(session_email)
    page.type_sign_in_password(session_password)
    page.click_sign_in_btn()
    common.click_addresses()
    addresses.click_on_element(AL.locator_new_address_link)
    addresses.set_data_to_field(AL.locator_first_name_field, "Andrii")
    addresses.set_data_to_field(AL.locator_last_name_field, "AQA")
    addresses.set_data_to_field(AL.locator_address1_field, "Street")
    addresses.set_data_to_field(AL.locator_address2_field, "Street2")
    addresses.set_data_to_field(AL.locator_city, "Lviv")
    addresses.select_dropdown_option(AL.locator_state, "Alaska")
    addresses.set_data_to_field(AL.locator_zip_code, "79000")
    addresses.click_on_element(AL.locator_address_country_us)
    addresses.set_data_to_field(AL.locator_birthday, "11.06.1985")
    addresses.set_data_to_field(AL.locator_color, "#00FF33")
    addresses.set_data_to_field(AL.locator_age, "35")
    addresses.set_data_to_field(AL.locator_website, "https://www.site.com")
    addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")
    addresses.set_data_to_field(AL.locator_phone, "123456")
    addresses.click_on_element(AL.locator_climbing)
    addresses.click_on_element(AL.locator_dancing)
    addresses.click_on_element(AL.locator_reading)
    addresses.set_data_to_field(AL.locator_note, "Test note")
    addresses.click_on_element(AL.locator_create_update_address_btn)
    dict_results = {}
    results = addresses.find_elements_by_locator(AL.locator_container_options)
    for element in results:
        key = element.find_element_by_xpath('.//span[1]')
        breakpoint()

        value = element.find_element_by_xpath('.//span[2]')
        dict_results[key] = value
        # key_data = web_element.find_element_by_locator(AL.locator_container_values_key)
        # list_keys.append(key_data)

    # assert addresses.find_element_by_locator(
    #     AL.locator_result_container).text.split('\n')[0]\
    #        == "Address was successfully created."
    addresses.click_on_element(AL.locator_show_list_link)
    addresses.click_on_element(AL.locator_destroy_address_link)
    popup = addresses.driver.switch_to.alert  # Not working
    popup.accept()
    time.sleep(2)


# def test_edit_addresses(browser_fixture):
#     addresses = AddressesSearchHelper(browser_fixture)
#     addresses.click_on_element(AL.locator_edit_address_link)
#     addresses.set_data_to_field(AL.locator_first_name_field, "2")
#     addresses.set_data_to_field(AL.locator_last_name_field, "2")
#     addresses.set_data_to_field(AL.locator_address1_field, "2")
#     addresses.set_data_to_field(AL.locator_address2_field, "2")
#     addresses.set_data_to_field(AL.locator_city, "2")
#     addresses.select_dropdown_option(AL.locator_state, "Arizona")
#     addresses.set_data_to_field(AL.locator_zip_code, "2")
#     addresses.click_on_element(AL.locator_address_country_canada)
#     addresses.set_data_to_field(AL.locator_birthday, "12.06.1985")
#     addresses.set_data_to_field(AL.locator_color, "#F58F00")
#     addresses.find_element_by_locator(AL.locator_age).send_keys(Keys.ARROW_UP)
#     addresses.find_element_by_locator(AL.locator_website).clear()
#     addresses.set_data_to_field(AL.locator_website, "https://www.site2.com")
#     addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\124.png")
#     addresses.set_data_to_field(AL.locator_phone, "2")
#     addresses.click_on_element(AL.locator_climbing)
#     addresses.click_on_element(AL.locator_dancing)
#     addresses.click_on_element(AL.locator_reading)
#     addresses.set_data_to_field(AL.locator_note, "2")
#     breakpoint()
#     addresses.click_on_element(AL.locator_create_update_address_btn)
#     assert addresses.find_element_by_locator(
#         AL.locator_result_container).text.split('\n')[0] \
#            == "Address was successfully updated."
#     addresses.click_on_element(AL.locator_show_list_link)





