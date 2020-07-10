import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser_fixture():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Andrii\\PycharmProjects\\"
                        "testaddressbook\\chromedriver.exe")
    yield driver
    driver.quit()
