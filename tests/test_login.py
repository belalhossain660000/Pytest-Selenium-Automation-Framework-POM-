# tests/test_login.py

import pytest
from pages.login_page import LoginPage
from utility import config
from utility.screenshot_utility import take_screenshot


def test_login(driver):
    """Test login functionality and capture a screenshot if it fails."""
    login_page = LoginPage(driver)

    try:

        login_page.enter_username(config.username)
        login_page.enter_password(config.password)
        login_page.click_login_button()

        login_page.login_successfull(config.login_assert_text)

    except Exception as e:
        take_screenshot(driver, "test_login_failure")
        pytest.fail(f"Test failed due to: {e}")
