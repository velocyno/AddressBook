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
            SignInLocators.locator_sign_in_page_tittle, time=2).text

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

    def click_on_sign_up_link(self):
        return self.find_element(
            SignInLocators.locator_sign_up_link, time=2).click()
