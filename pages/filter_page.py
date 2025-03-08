from pages.base_page import BasePage
from locators.filter_locators import FilterLocators
from tests.conftest import driver


class FilterProduct(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_filter_icon_dropdown(self):
        self.click_element(FilterLocators.FILTER_DROPDOWN)

    def select_high_to_low(self):
        self.click_element(FilterLocators.HIGH_TO_LOW)

    def verify_filter(self, filter_assert_text):
        fat = self.get_text(FilterLocators.FILTER_ASSERT)
        assert fat == filter_assert_text