import pytest
import json
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader


@pytest.fixture(scope="session")
def browser_fixture():
    chrome_driver = ChromeDriverDownloader()
    chrome_driver.download_and_install("83.0.4103.39")
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Andrii\\bin\\chromedriver.exe")
    yield driver
    driver.quit()

@pytest.fixture
def data_fixture():
    dict_data = {
        'First name:': 'Andrii',
        'Last name:': 'AQA',
        'Street Address:': 'Street',
        'Secondary Address:': 'Street2',
        'City:': 'Lviv',
        'State:': 'AK',
        'Zip code:': '79000',
        'Country:': 'us',
        'Birthday:': '6/11/1985',
        'Color:': "(0, 255, 51)",
        'Age:': '35',
        'Website:': 'https://www.site.com',
        'Phone:': '123456',
        'Climbing?': 'Yes',
        'Dancing?': 'Yes',
        'Reading?': 'Yes',
        'Note:': 'Test note'
    }
    return dict_data


@pytest.fixture
def data_fixture_js():
    json_file = open("../test_input_data/qa.json")
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()
