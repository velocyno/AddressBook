from pages.show_address_object import ShowAddressPage


class TestCreateAddress:
    def test_create_address(
        self, add_address_fixture, browser_fixture, data_fixture_js
    ):
        show_address_page = ShowAddressPage(browser_fixture)
        show_address_page.check_results_shown(data_fixture_js["dict_add_address"])
