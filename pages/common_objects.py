from base.base_page import BasePage
from selenium.webdriver.common.by import By


class NavbarLocators:
    locator_navbar_menu_items = (By.ID, "navbar")
    locator_sign_in_link = (By.ID, "sign-in")
    locator_sign_out_link = (By.XPATH, '//*[@id="navbar"]/div[1]/a[3]')
    locator_addresses_link = (By.LINK_TEXT, "Addresses")


class CommonSearchHelper(BasePage):
    def navbar_items(self):
        return self.find_element(
            NavbarLocators.locator_navbar_menu_items,
            time=self.light_load_element
        ).text.split()

    def click_sign_in(self):
        return self.find_element(
            NavbarLocators.locator_sign_in_link
        ).click()

    def click_sign_out(self):
        return self.find_element(
            NavbarLocators.locator_sign_out_link).click()

    def click_addresses(self):
        return self.find_element(
            NavbarLocators.locator_addresses_link,
            time=self.light_load_element
        ).click()
