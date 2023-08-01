from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(20)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
