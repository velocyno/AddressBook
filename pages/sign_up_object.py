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
            SignUpPageLocators.locator_sign_up_page_tittle, time=2).text

    def type_sign_up_email(self, email):
        self.email_field = self.find_element(
            SignUpPageLocators.locator_sign_up_email_field, time=2)
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_up_password(self, password):
        self.password_field = self.find_element(
            SignUpPageLocators.locator_sign_up_pass_field, time=2)
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_up_btn(self):
        return self.find_element(
            SignUpPageLocators.locator_sign_up_button, time=2).click()

    def click_on_sign_in_link(self):
        return self.find_element(
            SignUpPageLocators.locator_sign_in_link, time=2).click()
