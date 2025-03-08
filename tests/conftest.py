import pytest
from drivers.driver_factory import get_driver
from selenium.webdriver.common.by import By
import time
import os


# Fixture to initialize the WebDriver
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption('--browser')  # Get browser option from command line
    driver = get_driver(browser_name)
    driver.maximize_window()

    yield driver  # Yield driver to the test function

    driver.quit()  # After test, close the driver


# Adding a command-line option to select browser dynamically
def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Choose browser: chrome, firefox, edge'
    )
