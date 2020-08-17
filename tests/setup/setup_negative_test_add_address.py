from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader


class TestAddAddressNegative:

    # Question: Can I use PARAMETRIZE HERE?
    @classmethod
    def setup_class(cls):
        file = open("C:\\Users\\Andrii\\repositories\\AddressBook\\test_input_data\\qa.json")
        cls.data_gen = [json.load(file)]
        chrome_driver = ChromeDriverDownloader()
        driver_path = chrome_driver.download_and_install()
        cls.driver = webdriver.Chrome(
            executable_path=driver_path[0])
        session_email = cls.data_gen[0]["session_email"]
        session_password = cls.data_gen[0]["session_password"]
        page = SignInSearchHelper(cls.driver)
        common = CommonSearchHelper(cls.driver)
        addresses = AddressesSearchHelper(cls.driver)
        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()
        return cls.driver, cls.data_gen

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_error_required_fields_blank(
            self,
    ):
        addresses = AddressesSearchHelper(self.driver)
        # session_email = data_fixture_js["session_email"]
        # session_password = data_fixture_js["session_password"]
        # page = SignInSearchHelper(browser_fixture)
        # common = CommonSearchHelper(browser_fixture)
        # addresses = AddressesSearchHelper(browser_fixture)
        # page.go_to_sign_in_page()
        # page.type_sign_in_email(session_email)
        # page.type_sign_in_password(session_password)
        # page.click_sign_in_btn()
        # common.click_addresses()


        addresses.click_on_element(
            AL.locator_new_address_link
        )

        common = CommonSearchHelper(self.driver)
        # addresses = AddressesSearchHelper(self.driver)

        addresses.set_data_to_field(
            AL.locator_first_name_field,
            self.data_gen[0]['address_negative']['p1']['test_input']['first_name']
        )

        addresses.set_data_to_field(
            AL.locator_last_name_field,
            self.data_gen[0]['address_negative']['p1']['test_input']["last_name"]
        )

        addresses.set_data_to_field(
            AL.locator_address1_field,
            self.data_gen[0]['address_negative']['p1']['test_input']["address1"]
        )

        addresses.set_data_to_field(
            AL.locator_city,
            self.data_gen[0]['address_negative']['p1']['test_input']["city"]
        )

        addresses.set_data_to_field(
            AL.locator_zip_code,
            self.data_gen[0]['address_negative']['p1']['test_input']["zip_code"]
        )

        addresses.click_on_element(
            AL.locator_create_update_address_btn
        )

        error_message = common.get_text_from_element(
            AL.locator_required_fields_error
        )
        assert error_message == self.data_gen[0]['address_negative']['p1']["expected"]
        addresses.click_on_element(AL.locator_list_link)
