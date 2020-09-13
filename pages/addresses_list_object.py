from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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

        # self.wait_until_visible(
        #     (By.CLASS_NAME, "container")
        # )

        self.wait_until_text_in_element(
            (By.LINK_TEXT, "List"),
            "List"
        )

    def click_destroy_link(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_all_elements_located(
        #         (By.XPATH, "//td"),
        #     ),
        #     message=f"Locator is not visible"
        # )
        # time.sleep(2)

        self.find_element(
            (By.XPATH, "//tr")
        )

        self.find_elements(
            (By.XPATH, "//td")
        )

        self.wait_until_text_in_element(
            (By.LINK_TEXT, "Show"),
            "Show"
        )

        self.wait_until_text_in_element(
            (By.LINK_TEXT, "Edit"),
            "Edit"
        )

        destroy_link = self.driver.find_element(
            By.LINK_TEXT, "Destroy"
        )

        destroy_link.click()

        self.wait_until_alert_appear()

    def click_ok_on_alert(self):
        self.wait_until_alert_appear()

        popup = self.driver.switch_to.alert

        popup.accept()

        self.wait_until_alert_disappear()

        self.wait_until_text_in_element(
            (By.LINK_TEXT, "New Address"),
            "New Address"
        )

        self.wait_until_visible(
            (By.CLASS_NAME, "table")
        )
