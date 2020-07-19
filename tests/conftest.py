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
    json_file = open("../test_input_data/qa.json")
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()
