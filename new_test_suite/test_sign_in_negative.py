from pages.sign_in_object import SignInSearchHelper
import pytest
import random
import string


class TestSignInNegative:

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
        session_email = test_input["email"]
        session_password = test_input["password"]
        sign_in_page = SignInSearchHelper(browser_fixture)

        sign_in_page.go_to_sign_in_page()
        sign_in_page.provide_credentials(session_email, session_password)
        sign_in_page.check_error_message(expected)
        sign_in_page.check_usrer_is_not_logged_in(session_email)

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
        sign_in_page.go_to_sign_in_page()
        sign_in_page.provide_credentials(session_email, session_password)
        sign_in_page.check_email_field_is_active()
        sign_in_page.check_usrer_is_not_logged_in(session_email)
