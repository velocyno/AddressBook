import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser_fixture():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Andrii\\repositories\\"
                        "AddressBook\\chromedriver.exe")
    # ../ chromedriver.exe
    yield driver
    driver.quit()
