from pages.sign_in_object import SignInSearchHelper
from pages.sign_up_object import SignUpSearchHelper
from pages.common_objects import CommonSearchHelper
from pages.adresses_object import AddressesLocators as AL
from pages.adresses_object import AddressesSearchHelper
from selenium.common.exceptions import TimeoutException
from tests.test_helper import CreateUser
import pytest
import random
import string

class TestSignInNegative:
    user_created = False

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                    {
                        "email": "",  # blank email and password
                        "password": ""
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymail@i.ua",  # existed user and blank password
                        "password": ""
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymail@i.ua",  # existed user and incorrect password
                        "password": "111111"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "",  # blank email with valid password
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        # unregistered user
                        "email": "".join(random.choices(string.ascii_lowercase, k=6)) + "@i.ua",
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
        ]
    )
    def test_sign_in_invalid_email_password(
            self,
            browser_fixture,
            data_fixture_js,
            test_input,
            expected
    ):
        if not TestSignInNegative.user_created:
            create_user = CreateUser()
            create_user.create_user(browser_fixture)
            TestSignInNegative.user_created = True
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_in_page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.type_sign_in_email(session_email)
        sign_in_page.type_sign_in_password(session_password)
        sign_in_page.click_sign_in_btn()
        error_message = sign_in_page.error_message()
        assert error_message == expected
        assert session_email not in common.navbar_items()

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (
                    {
                        "email": "mymaili.ua",  # email without @ sign
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymail@i",  # email without TLD
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymail@i.",  # email with dot without TLD
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymaili@.com",  # email without TLD
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymaili@",  # email without TLD
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        "email": "mymaili",  # email without TLD
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
        ]
    )
    def test_sign_in_bad_email_format(
            self,
            browser_fixture,
            test_input,
            expected
    ):
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_in_page = SignInSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.type_sign_in_email(session_email)
        sign_in_page.type_sign_in_password(session_password)
        sign_in_page.click_sign_in_btn()
        email_field = sign_in_page.driver.switch_to_active_element()
        header = sign_in_page.sign_in_page_header()
        placeholder = email_field.get_attribute("placeholder")
        assert session_email not in common.navbar_items()
        assert header == "Sign in"
        assert placeholder == "Email"
