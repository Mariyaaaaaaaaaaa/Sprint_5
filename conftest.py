import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = "../chromedriver"

@pytest.fixture(scope="function")
def driver():
    service = Service(executable_path=DRIVER_PATH)
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()