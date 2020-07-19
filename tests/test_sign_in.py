from pages.sign_in_object import SignInSearchHelper
from pages.sign_up_object import SignUpSearchHelper
from pages.common_objects import CommonSearchHelper


class TestSignInPage:
    def test_sign_in_page_header(self, browser_fixture):
        address_main_page = CommonSearchHelper(browser_fixture)
        sign_in_page = SignInSearchHelper(browser_fixture)
        address_main_page.go_to_home_page()
        address_main_page.click_sign_in()
        assert sign_in_page.sign_in_page_header() == "Sign in"

    def test_sign_up_link(self, browser_fixture):
        sign_in_page = SignInSearchHelper(browser_fixture)
        sign_up_page = SignUpSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.click_on_sign_up_link()
        assert sign_up_page.sign_up_page_header() == "Sign up"

    def test_sign_in(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email"]
        session_password = data_fixture_js["session_password"]
        sign_in_page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.type_sign_in_email(session_email)
        sign_in_page.type_sign_in_password(session_password)
        sign_in_page.click_sign_in_btn()
        assert session_email in common.navbar_items()
        common.click_sign_out()

    def test_sign_out(self, browser_fixture, data_fixture_js):
        session_email = data_fixture_js["session_email"]
        session_password = data_fixture_js["session_password"]
        sign_in_page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.type_sign_in_email(session_email)
        sign_in_page.type_sign_in_password(session_password)
        sign_in_page.click_sign_in_btn()
        common.click_sign_out()
        assert session_email not in common.navbar_items()
