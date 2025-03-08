import pytest
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCartPage
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

def test_add_to_cart(driver, login):

    try:
        add_to_cart_page = AddToCartPage(driver)
        add_to_cart_page.add_product_to_cart()
        add_to_cart_page.got_to_cart()
        add_to_cart_page.click_on_checkout_button()
        add_to_cart_page.checkout_done(config.verify_element_assert_text)

    except Exception as e:
        take_screenshot(driver, "test_add_to_cart_failure")
        pytest.fail(f"Test failed due to: {e}")
