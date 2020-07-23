from base.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPageLocators:
    locator_sign_up_page_tittle = (By.CLASS_NAME, "text-center")
    locator_sign_up_email_field = (By.ID, "user_email")
    locator_sign_up_pass_field = (By.ID, "user_password")
    locator_sign_up_button = (By.XPATH, '//*[@id="new_user"]/div[3]/input')
    locator_sign_in_link = (By.LINK_TEXT, "Sign in")


class SignUpSearchHelper(BasePage):
    def sign_up_page_header(self):
        return self.find_element(
            SignUpPageLocators.locator_sign_up_page_tittle,
            time=self.light_load_element
        ).text

    def type_sign_up_email(self, email):
        self.email_field = self.find_element(
            SignUpPageLocators.locator_sign_up_email_field,
            time=self.light_load_element
        )
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_up_password(self, password):
        self.password_field = self.find_element(
            SignUpPageLocators.locator_sign_up_pass_field,
            time=self.light_load_element
        )
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_up_btn(self):
        return self.find_element(
            SignUpPageLocators.locator_sign_up_button,
            time=self.light_load_element
        ).click()

    def click_on_sign_in_link(self):
        return self.find_element(
            SignUpPageLocators.locator_sign_in_link,
            time=self.light_load_element
        ).click()
