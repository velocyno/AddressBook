import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriverdownloader import ChromeDriverDownloader
import pathlib


# @pytest.fixture(scope="session")
# def browser_fixture():
#     chrome_driver = ChromeDriverDownloader()
#     driver_path = chrome_driver.download_and_install()
#     driver = webdriver.Chrome(
#         executable_path=driver_path[0])
#     yield driver
#     driver.quit()

@pytest.fixture(scope="session")
def browser_fixture():
    my_desired_capabilities = DesiredCapabilities.CHROME.copy()
    chrome_options_remote = webdriver.ChromeOptions()
    chrome_options_remote.add_argument("--start-maximized")

    init_remote_driver = webdriver.Remote(
        options=chrome_options_remote,
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=my_desired_capabilities
    )
    return init_remote_driver

@pytest.fixture(scope="session")
def browser_fixture():
    my_desired_capabilities = DesiredCapabilities.CHROME.copy()
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=my_desired_capabilities
    )
    yield driver
    driver.quit()

# @pytest.fixture
# def data_fixture_js():
#     json_file = open("../test_input_data/qa.json")
#     data_from_file = json.load(json_file)
#     yield data_from_file
#     json_file.close()

@pytest.fixture
def data_fixture_js():
    cur_path = pathlib.Path(__file__).parent
    json_file = open(f'{cur_path}\\test_input_data\\qa.json')
    data_from_file = json.load(json_file)
    yield data_from_file
    json_file.close()


# used in generator tests
def pytest_generate_tests(metafunc):
    if "data_gen" in metafunc.fixturenames:
        cur_path = pathlib.Path(__file__).parent
        # file = open("../test_input_data/qa.json")
        file = open(f'{cur_path}\\test_input_data\\qa.json')
        data = [json.load(file)]
        metafunc.parametrize("data_gen", [
            data[0]["address_negative"]["p1"],
            data[0]["address_negative"]["p2"]
            ]
        )
