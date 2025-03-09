from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
import os


def get_driver(browser_name='chrome'):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        # options.add_argument('--headless')  # Remove this for running with UI
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        # options.add_argument('--headless')  # Remove this for running with UI
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser_name == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        # options.add_argument('--headless')  # Remove this for running with UI
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    return driver
