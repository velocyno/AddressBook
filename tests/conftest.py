import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader


@pytest.fixture(scope="session")
def browser_fixture():
    chrome_driver = ChromeDriverDownloader()
    driver_path = chrome_driver.download_and_install()
    driver = webdriver.Chrome(
        executable_path=driver_path[0])
    yield driver
    driver.quit()


@pytest.fixture
def data_fixture_js():
    # json_file = open("../test_input_data/qa.json")
    json_file = open("C:\\Users\\Andrii\\repositories\\AddressBook\\test_input_data\\qa.json")
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


# used in generator tests
def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        file = open("C:\\Users\\Andrii\\repositories\\AddressBook"
                    "\\test_input_data\\qa.json")
        data = [json.load(file)]
        metafunc.parametrize("data_gen", [
            data[0]["address_negative"]["p1"],
            data[0]["address_negative"]["p2"]
            ]
        )
