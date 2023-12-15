import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.main_page_url)

    yield driver
    driver.quit()

