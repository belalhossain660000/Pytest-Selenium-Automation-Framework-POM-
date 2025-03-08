# pages/base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utility.screenshot_utility import take_screenshot

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit wait of 10 seconds

    def find_element(self, locator):
        """Find an element using an XPath locator."""
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            print(f"Timeout: Element {locator} not found")
            return None
        except NoSuchElementException:
            print(f"Error: Element {locator} not found")
            return None

    def click_element(self, locator):
        """Click an element after waiting for it to be clickable."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
        except TimeoutException:
            print(f"Timeout: Unable to click element {locator}")

    def enter_text(self, locator, text):
        """Enter text into an input field."""
        element = self.find_element(locator)
        if element:
            element.clear()  # Clear existing text
            element.send_keys(text)

    def get_text(self, locator):
        """Retrieve text from an element."""
        element = self.find_element(locator)
        return element.text if element else None

    def take_screenshot(self, name):
        """Capture a screenshot."""
        take_screenshot(self.driver, name)

    def is_element_present(self, locator):
        """Check if an element is present on the page."""
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except NoSuchElementException:
            return False
