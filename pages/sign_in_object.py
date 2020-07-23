from base.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInLocators:
    locator_sign_in_page_tittle = (By.TAG_NAME, "h2")
    locator_sign_in_email_field = (By.ID, "session_email")
    locator_sign_in_pass_field = (By.ID, "session_password")
    locator_sign_in_button = (By.XPATH, '//*[@id="clearance"]/div/div'
                                        '/form/div[3]/input')
    locator_sign_up_link = (By.LINK_TEXT, "Sign up")


class SignInSearchHelper(BasePage):
    def sign_in_page_header(self):
        return self.find_element(
            SignInLocators.locator_sign_in_page_tittle,
            time=self.light_load_element
        ).text

    def type_sign_in_email(self, email):
        self.email_field = self.find_element(
            SignInLocators.locator_sign_in_email_field,
            time=self.light_load_element
        )
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_in_password(self, password):
        self.password_field = self.find_element(
            SignInLocators.locator_sign_in_pass_field,
            time=self.light_load_element
        )
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_in_btn(self):
        return self.find_element(
            SignInLocators.locator_sign_in_button,
            time=self.light_load_element
        ).click()

    def click_on_sign_up_link(self):
        return self.find_element(
            SignInLocators.locator_sign_up_link,
            time=self.light_load_element
        ).click()
