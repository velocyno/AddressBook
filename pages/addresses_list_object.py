from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressesListLocators:
    locator_new_address_link = (By.LINK_TEXT, "New Address")
    locator_show_address_link = (By.LINK_TEXT, "Show")
    locator_edit_address_link = (By.LINK_TEXT, "Edit")
    locator_destroy_address_link = (By.LINK_TEXT, "Destroy")
    locator_destroyed_message = (By.XPATH, "/html/body/div/div")
    locator_create_update_address_btn = (By.NAME, "commit")


class AddressesListPage(BasePage):
    def click_new_address_link(self):
        self.wait_until_text_in_element(
            (By.LINK_TEXT, "New Address"),
            "New Address"
        )

        new_address_link = self.driver.find_element(
            By.LINK_TEXT, "New Address"
        )

        new_address_link.click()

        self.wait_until_text_in_element(
            (By.TAG_NAME, "h2"),
            "New Address"
        )

    def click_show_address_link(self):
        self.wait_until_text_in_element(
            (By.LINK_TEXT, "Show"),
            "Show"
        )

        show_link = self.driver.find_element(
            By.LINK_TEXT, "Show"
        )

        show_link.click()

        self.wait_until_visible(
            (By.CLASS_NAME, "container")
        )

    def click_destroy_link(self):
        self.wait_until_text_in_element(
            (By.LINK_TEXT, "Destroy"),
            "Destroy"
        )

        destroy_link = self.driver.find_element(
            By.LINK_TEXT, "Destroy"
        )

        return destroy_link.click()
        # breakpoint()

        # self.wait_until_alert_appear()

    def click_ok_on_alert(self):
        self.wait_until_alert_appear()
        popup = self.driver.switch_to.alert
        popup.accept()
        self.wait_until_alert_disappear()
