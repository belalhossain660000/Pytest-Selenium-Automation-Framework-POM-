from pages.base_page import BasePage
from locators.add_to_cart_locators import AddToCartLocators

class AddToCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        self.click_element(AddToCartLocators.ADD_TO_CART_BUTTON)

    def got_to_cart(self):
        self.click_element(AddToCartLocators.CART_ICON)

    def click_on_checkout_button(self):
        self.click_element(AddToCartLocators.CHECKOUT_BUTTON)

    def checkout_done(self, verify_element):
        ctdt = self.get_text(AddToCartLocators.VERIFY_ELEMENT)
        assert ctdt == verify_element

