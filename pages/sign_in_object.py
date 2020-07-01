from base.base_page import BasePage
from selenium.webdriver.common.by import By


# from pages.common_objects import CommonSearchHelper


class SignInLocators:
    locator_sign_in_email_field = (By.ID, "session_email")
    locator_sign_in_pass_field = (By.ID, "session_password")
    locator_sign_in_button = (By.XPATH, '//*[@id="clearance"]/div/div'
                                        '/form/div[3]/input')


class SignInSearchHelper(BasePage):
    def type_sign_in_email(self, email):
        self.email_field = self.find_element(
            SignInLocators.locator_sign_in_email_field, time=2)
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_in_password(self, password):
        self.password_field = self.find_element(
            SignInLocators.locator_sign_in_pass_field, time=2)
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_in_btn(self):
        return self.find_element(
            SignInLocators.locator_sign_in_button, time=2).click()
