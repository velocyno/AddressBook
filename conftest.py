import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
from tests.test_helper import TestHelper
import pathlib
import requests


@pytest.fixture(scope="class")
def browser_fixture():
    chrome_driver = ChromeDriverDownloader()
    driver_path = chrome_driver.download_and_install()
    driver = webdriver.Chrome(executable_path=driver_path[0])
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def data_fixture_js():
    cur_path = pathlib.Path(__file__).parent
    json_file = open(f"{cur_path}/test_input_data/qa.json")
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


@pytest.fixture(scope="class")
def log_in(browser_fixture, data_fixture_js):
    log_in_helper = TestHelper.LogIn()
    email = log_in_helper.log_in(browser_fixture, data_fixture_js)
    yield email


@pytest.fixture(scope="function")
def add_address_fixture(browser_fixture, data_fixture_js, delete_address):
    add_address_helper = TestHelper.AddAddress()
    address_url = add_address_helper.add_address(
        browser_fixture, data_fixture_js, delete_address
    )
    yield address_url


@pytest.fixture
def delete_address():
    addresses_to_delete = {"address": [], "headers": ""}
    yield addresses_to_delete
    for address in addresses_to_delete["address"]:
        requests.delete(address, headers=addresses_to_delete["headers"])


def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        cur_path = pathlib.Path(__file__).parent
        file = open(f"{cur_path}/test_input_data/qa.json")
        data = [json.load(file)]
        metafunc.parametrize(
            "data_gen",
            [data[0]["address_negative"]["p1"], data[0]["address_negative"]["p2"]],
        )
