import unittest
from selenium import webdriver
from pages.home_sign_up_object import SearchHelper


class AddressTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        self.driver.get("http://a.testaddressbook.com/")

    def test_1(self):
        address_main_page = SearchHelper(self.driver)
        address_main_page.go_to_home_page()
        home_header = address_main_page.home_page_header()
        compare_header = "Welcome to Address Book\n\nA simple web app" \
                               " for showing off your testing"
        self.assertEqual(home_header.text, compare_header)
        # pass


    def tearDown(self):
        self.driver.quit()
