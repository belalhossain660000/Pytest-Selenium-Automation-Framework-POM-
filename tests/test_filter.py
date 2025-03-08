import pytest
from pages.login_page import LoginPage
from pages.filter_page import FilterProduct
from utility.screenshot_utility import take_screenshot
from utility import config

@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username(config.username)
    login_page.enter_password(config.password)
    login_page.click_login_button()
    login_page.login_successfull(config.login_assert_text)
    return login_page


def test_filter_product(driver, login):

    try:
        filter_product = FilterProduct(driver)
        filter_product.click_on_filter_icon_dropdown()
        filter_product.select_high_to_low()
        filter_product.verify_filter(config.filter_assert_text)

    except Exception as e:
        take_screenshot(driver, "test_filter_failure")
        pytest.fail(f"Test failed due to: {e}")
