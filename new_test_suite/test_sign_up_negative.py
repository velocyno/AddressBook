from pages.sign_up_object import SignUpSearchHelper
from pages.common_objects import CommonSearchHelper
from tests.test_helper import TestHelper
import random
import string
import pytest


class TestSignUpNegative:

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
                        "email": "mymail@i.ua",  # existed user and valid password
                        "password": "123456"
                    },
                    "Bad email or password."
            ),
            (
                    {
                        # new user and blank password
                        "email": "".join(random.choices(string.ascii_lowercase, k=6)) + "@i.ua",
                        "password": ""
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
        ]
    )
    def test_sign_up_invalid_email_password(
            self,
            browser_fixture,
            data_fixture_js,
            test_input,
            expected
    ):
        sign_up_email = test_input["email"]
        sign_up_password = test_input["password"]
        sign_up_page = SignUpSearchHelper(browser_fixture)
        # common = CommonSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.provide_sign_up_credentials(sign_up_email, sign_up_password)
        sign_up_page.check_usrer_is_not_logged_in(sign_up_email)

        # assert sign_up_email not in common.navbar_items()

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
    def test_sign_up_bad_email_format(
            self,
            browser_fixture,
            test_input,
            expected
    ):
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_up_page = SignUpSearchHelper(browser_fixture)
        common = CommonSearchHelper(browser_fixture)
        sign_up_page.go_to_sign_up_page()
        sign_up_page.type_sign_up_email(session_email)
        sign_up_page.type_sign_up_password(session_password)
        sign_up_page.click_sign_up_btn()
        email_field = sign_up_page.driver.switch_to_active_element()
        header = sign_up_page.sign_up_page_header()
        placeholder = email_field.get_attribute("placeholder")
        assert session_email not in common.navbar_items()
        assert header == "Sign up"
        assert placeholder == "Email"
