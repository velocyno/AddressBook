import pytest
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader


@pytest.fixture(scope="session")
def browser_fixture():
    chrome_driver = ChromeDriverDownloader()
    chrome_driver.download_and_install()
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Andrii\\bin\\chromedriver.exe")
    yield driver
    driver.quit()