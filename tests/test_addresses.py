from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import Converters
import time

dict_data = {
    'First name:': 'Andrii',
    'Last name:': 'AQA',
    'Street Address:': 'Street',
    'Secondary Address:': 'Street2',
    'City:': 'Lviv',
    'State:': 'AK',
    'Zip code:': '79000',
    'Country:': 'us',
    'Birthday:': '6/11/1985',
    'Color:': "(0, 255, 51)",
    'Age:': '35',
    'Website:': 'https://www.site.com',
    'Phone:': '123456',
    'Climbing?': 'Yes',
    'Dancing?': 'Yes',
    'Reading?': 'Yes',
    'Note:': 'Test note'
}

def test_add_address(browser_fixture):
    session_email = "andrii1@i.ua"
    session_password = "123456"
    page = SignInSearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)
    addresses = AddressesSearchHelper(browser_fixture)
    converter = Converters()
    page.go_to_sign_in_page()
    page.type_sign_in_email(session_email)
    page.type_sign_in_password(session_password)
    page.click_sign_in_btn()
    common.click_addresses()
    addresses.click_on_element(AL.locator_new_address_link)
    addresses.set_data_to_field(AL.locator_first_name_field, dict_data["First name:"])
    addresses.set_data_to_field(AL.locator_last_name_field, dict_data["Last name:"])
    addresses.set_data_to_field(AL.locator_address1_field, dict_data["Street Address:"])
    addresses.set_data_to_field(AL.locator_address2_field, dict_data["Secondary Address:"])
    addresses.set_data_to_field(AL.locator_city, dict_data["City:"])
    addresses.select_dropdown_option(AL.locator_state, dict_data["State:"])
    addresses.set_data_to_field(AL.locator_zip_code, dict_data["Zip code:"])
    addresses.select_state(dict_data["Country:"])
    addresses.set_data_to_field(AL.locator_birthday, converter.date_converter(dict_data["Birthday:"]))
    addresses.set_data_to_field(AL.locator_color, converter.rgb_to_hex(dict_data["Color:"]))
    addresses.set_data_to_field(AL.locator_age, dict_data["Age:"])
    addresses.set_data_to_field(AL.locator_website, dict_data["Website:"])
    # addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")
    addresses.set_data_to_field(AL.locator_phone, dict_data["Phone:"])
    addresses.click_on_element_if_yes(AL.locator_climbing, dict_data["Climbing?"])
    addresses.click_on_element_if_yes(AL.locator_dancing, dict_data["Dancing?"])
    addresses.click_on_element_if_yes(AL.locator_reading, dict_data["Reading?"])
    addresses.set_data_to_field(AL.locator_note, dict_data["Note:"])
    addresses.click_on_element(AL.locator_create_update_address_btn)
    dict_results = {}
    results = addresses.find_elements_by_locator(AL.locator_container_options)
    for element in results:
        key = element.find_element_by_xpath('.//span[1]').text
        value = element.find_element_by_xpath('.//span[2]').text
        if key == 'Color:':
            value = element.find_element_by_xpath('.//span[2]')
            value = value.get_attribute('style').split("rgb")[1].rstrip(";")
        dict_results[key] = value
    assert addresses.find_element_by_locator(
        AL.locator_result_container).text.split('\n')[0]\
           == "Address was successfully created."
    assert dict_data == dict_results
    addresses.click_on_element(AL.locator_show_list_link)
    # addresses.click_on_element(AL.locator_destroy_address_link)
    # popup = addresses.driver.switch_to.alert
    # popup.accept()
    # time.sleep(2)

dict_data_edit = {
    'First name:': 'Andrii2',
    'Last name:': 'AQA2',
    'Street Address:': 'Street2',
    'Secondary Address:': 'Street22',
    'City:': 'Lviv2',
    'State:': 'AZ',
    'Zip code:': '790002',
    'Country:': 'canada',
    'Birthday:': '6/12/1985',
    'Color:': "(25, 150, 245)",
    'Age:': '36',
    'Website:': 'https://www.site2.com',
    'Phone:': '123-4562',
    'Climbing?': 'No',
    'Dancing?': 'No',
    'Reading?': 'No',
    'Note:': 'Test note2'
}


def test_edit_addresses(browser_fixture):
    addresses = AddressesSearchHelper(browser_fixture)
    addresses.click_on_element(AL.locator_edit_address_link)
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
    addresses.set_data_to_field(AL.locator_first_name_field, dict_data_edit["First name:"])
    addresses.set_data_to_field(AL.locator_last_name_field, dict_data_edit["Last name:"])
    addresses.set_data_to_field(AL.locator_address1_field, dict_data_edit["Street Address:"])
    addresses.set_data_to_field(AL.locator_address2_field, dict_data_edit["Secondary Address:"])
    addresses.set_data_to_field(AL.locator_city, dict_data_edit["City:"])
    addresses.select_dropdown_option(AL.locator_state, dict_data_edit["State:"])
    addresses.set_data_to_field(AL.locator_zip_code, dict_data_edit["Zip code:"])
    addresses.select_state(dict_data_edit["Country:"])
    addresses.set_data_to_field(AL.locator_birthday, converter.date_converter(dict_data_edit["Birthday:"]))
    addresses.set_data_to_field(AL.locator_color, converter.rgb_to_hex(dict_data_edit["Color:"]))
    addresses.set_data_to_field(AL.locator_age, dict_data_edit["Age:"])
    addresses.set_data_to_field(AL.locator_website, dict_data_edit["Website:"])
    # addresses.find_element_by_locator(AL.locator_picture).send_keys("C:\\123.png")
    addresses.set_data_to_field(AL.locator_phone, dict_data_edit["Phone:"])
    addresses.click_on_element_if_yes(AL.locator_climbing, dict_data_edit["Climbing?"])
    addresses.click_on_element_if_yes(AL.locator_dancing, dict_data_edit["Dancing?"])
    addresses.click_on_element_if_yes(AL.locator_reading, dict_data_edit["Reading?"])
    addresses.set_data_to_field(AL.locator_note, dict_data_edit["Note:"])
    addresses.click_on_element(AL.locator_create_update_address_btn)
    dict_results = {}
    results = addresses.find_elements_by_locator(AL.locator_container_options)
    for element in results:
        key = element.find_element_by_xpath('.//span[1]').text
        value = element.find_element_by_xpath('.//span[2]').text
        if key == 'Color:':
            value = element.find_element_by_xpath('.//span[2]')
            value = value.get_attribute('style').split("rgb")[1].rstrip(";")
        dict_results[key] = value
    assert addresses.find_element_by_locator(
        AL.locator_result_container).text.split('\n')[0] \
           == "Address was successfully updated."
    assert dict_data_edit == dict_results
    addresses.click_on_element(AL.locator_show_list_link)
    addresses.click_on_element(AL.locator_destroy_address_link)
    popup = addresses.driver.switch_to.alert
    popup.accept()
    time.sleep(2)



