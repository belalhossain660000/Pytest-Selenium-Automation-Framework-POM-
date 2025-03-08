from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utility.config import BASE_URL
from drivers.driver_factory import get_driver
from time import sleep


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(BASE_URL)

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def login_successfull(self, assert_text):
        sleep(4)
        at = self.get_text(LoginLocators.ASSERT_ELEMENT)
        assert at == assert_text
