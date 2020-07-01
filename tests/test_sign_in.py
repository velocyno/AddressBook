from pages.sign_in_object import SignInSearchHelper
from pages.common_objects import CommonSearchHelper


def test_sign_in(browser_fixture):
    session_email = "andrii1@i.ua"
    session_password = "123456"
    page = SignInSearchHelper(browser_fixture)
    common = CommonSearchHelper(browser_fixture)  # is it correct
    page.go_to_sign_in_page()
    page.type_sign_in_email(session_email)
    page.type_sign_in_password(session_password)
    page.click_sign_in_btn()
    assert session_email in common.navbar_items()
    common.click_sign_out()
    assert session_email not in common.navbar_items()

