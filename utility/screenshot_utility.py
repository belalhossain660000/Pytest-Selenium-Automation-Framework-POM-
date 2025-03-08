import os
from datetime import datetime


def take_screenshot(driver, test_name):
    """Capture a screenshot and save it in the 'screenshot' directory."""
    screenshot_dir = "F:\Sauce Demo POM FrameWork\screenshot"  # Ensure this matches your existing folder name
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)  # Create folder if missing

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
