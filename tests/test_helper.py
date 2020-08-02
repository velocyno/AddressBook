from selenium.common.exceptions import TimeoutException
from pages.sign_up_object import SignUpSearchHelper
from pages.common_objects import CommonSearchHelper


class CreateUser:
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