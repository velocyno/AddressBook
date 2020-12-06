from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.addresses_list_object import AddressesListPage
from pages.new_address_object import NewAddressLocators as NAL
from pages.new_address_object import NewAddressPage
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
import pathlib


class TestAddAddressNegative:

    # Question: Can I use PARAMETRIZE HERE?
    @classmethod
    def setup_class(cls):
        cur_path = pathlib.Path(__file__).parent
        cls.file = open(f"{cur_path}\\..\\..\\test_input_data\\qa.json")
        cls.data_gen = [json.load(cls.file)]
        chrome_driver = ChromeDriverDownloader()
        driver_path = chrome_driver.download_and_install()
        cls.driver = webdriver.Chrome(executable_path=driver_path[0])
        session_email = cls.data_gen[0]["session_email"]
        session_password = cls.data_gen[0]["session_password"]
        page = SignInSearchHelper(cls.driver)
        common = CommonSearchHelper(cls.driver)
        page.go_to_sign_in_page()
        page.type_sign_in_email(session_email)
        page.type_sign_in_password(session_password)
        page.click_sign_in_btn()
        common.click_addresses()
        return cls.driver, cls.data_gen

    @classmethod
    def teardown_class(cls):
        cls.file.close()
        cls.driver.quit()
        # Do I need some special clean up here (e.g. Log out, ...)

    def test_error_required_fields_blank(
        self,
    ):
        addresses_list_page = AddressesListPage(self.driver)
        new_address_page = NewAddressPage(self.driver)
        common = CommonSearchHelper(self.driver)

        addresses_list_page.click_new_address_link()

        new_address_page.set_data_to_field(
            NAL.locator_first_name_field,
            self.data_gen[0]["address_negative"]["p1"]["test_input"]["first_name"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_last_name_field,
            self.data_gen[0]["address_negative"]["p1"]["test_input"]["last_name"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_address1_field,
            self.data_gen[0]["address_negative"]["p1"]["test_input"]["address1"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_city,
            self.data_gen[0]["address_negative"]["p1"]["test_input"]["city"],
        )

        new_address_page.set_data_to_field(
            NAL.locator_zip_code,
            self.data_gen[0]["address_negative"]["p1"]["test_input"]["zip_code"],
        )

        new_address_page.click_create_address_btn()

        error_message = common.get_text_from_element(NAL.locator_required_fields_error)
        assert error_message == self.data_gen[0]["address_negative"]["p1"]["expected"]
