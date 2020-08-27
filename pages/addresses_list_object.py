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
    pass
