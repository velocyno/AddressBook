from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from pages.adresses_object import Converters
import time
from tests.test_helper import TestHelper


class TestEditAddressNegative:
    def test_edit_address_negative(self, browser_fixture, data_fixture_js):
        test_helper = TestHelper()
        test_helper.create_user(browser_fixture)
        test_helper.add_address(browser_fixture, data_fixture_js)
