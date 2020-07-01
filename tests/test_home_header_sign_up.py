from pages.home_sign_up_object import SearchHelper
from pages.common_objects import CommonSearchHelper
import random
import string


def test_home_page_header(browser_fixture):
    address_main_page = SearchHelper(browser_fixture)
    address_main_page.go_to_home_page()
    assert address_main_page.home_page_header() == "Welcome to Address Book" \
                        "\n\nA simple web app for showing off your testing"


def test_sign_in_page_header(browser_fixture):
    address_main_page = SearchHelper(browser_fixture)
    address_main_page.go_to_home_page()
    address_main_page.click_on_signin()
    assert address_main_page.signin_header() == "Sign in"


def test_sign_up(browser_fixture):
    sign_up_email = "".join(random.choices(string.ascii_lowercase, k=6))\
                    + "@i.ua"
    sign_up_password = "".join(random.choices(string.ascii_lowercase, k=6))
    page = SearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)
    page.go_to_sign_up_page()
    page.type_sign_up_email(sign_up_email)
    page.type_sign_up_password(sign_up_password)
    page.click_sign_up_btn()
    assert sign_up_email in common.navbar_items()
    common.click_sign_out()
    assert sign_up_email not in common.navbar_items()
