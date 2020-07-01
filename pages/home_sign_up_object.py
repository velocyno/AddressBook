from base.base_page import BasePage
from selenium.webdriver.common.by import By


class HomeSignUpLocators:
    # Home page
    locator_home_page_tittle = (By.CLASS_NAME, "text-center")
    # Sign in page
    locator_sign_in_page_tittle = (By.TAG_NAME, "h2")
    locator_sign_in_button = (By.ID, "sign-in")
    #Sign up page
    locator_sign_up_email_field = (By.ID, "user_email")
    locator_sign_up_pass_field = (By.ID, "user_password")
    locator_sign_up_button = (By.XPATH, '//*[@id="new_user"]/div[3]/input')
    # Header menu
    # locator_sign_out = (By.XPATH, '//*[@id="navbar"]/div[1]/a[3]')
    # locator_navbar_menu = (By.ID, "navbar")


class SearchHelper(BasePage):
    def click_on_signin(self):
        return self.find_element(
            HomeSignUpLocators.locator_sign_in_button, time=2).click()

    def home_page_header(self):
        return self.find_element(
            HomeSignUpLocators.locator_home_page_tittle, time=2).text

    def signin_header(self):
        return self.find_element(
            HomeSignUpLocators.locator_sign_in_page_tittle, time=2).text

    def type_sign_up_email(self, email):
        self.email_field = self.find_element(
            HomeSignUpLocators.locator_sign_up_email_field, time=2)
        self.email_field.send_keys(email)
        return self.email_field

    def type_sign_up_password(self, password):
        self.password_field = self.find_element(
            HomeSignUpLocators.locator_sign_up_pass_field, time=2)
        self.password_field.send_keys(password)
        return self.password_field

    def click_sign_up_btn(self):
        return self.find_element(
            HomeSignUpLocators.locator_sign_up_button, time=2).click()

    # def navbar_items(self):
    #     return self.find_element(
    #         HomeSignUpLocators.locator_navbar_menu, time=2).text.split()
    #
    # def click_sign_out(self):
    #     return self.find_element(HomeSignUpLocators.locator_sign_out).click()
