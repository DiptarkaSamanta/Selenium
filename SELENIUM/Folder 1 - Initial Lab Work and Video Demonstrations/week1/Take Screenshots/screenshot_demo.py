from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime

# Generic reusable method to take screenshots
def take_screenshot(driver, action_name="screenshot"):
    """
    Generic method to capture timestamped screenshots and store them in a dedicated folder.
    
    :param driver: WebDriver instance
    :param action_name: Custom name or label for the screenshot file
    :return: Absolute file path of the saved screenshot
    """
    screenshot_dir = os.path.join(os.getcwd(), "captured_screenshots")
    
    # Auto-create directory if missing
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
        print(f"Created directory: {screenshot_dir}")

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{action_name}_{timestamp}.png"
    full_file_path = os.path.join(screenshot_dir, file_name)

    # Save screenshot
    success = driver.save_screenshot(full_file_path)
    if success:
        print(f"[SUCCESS] Screenshot captured: {full_file_path}")
    else:
        print(f"[ERROR] Failed to capture screenshot.")
    
    return full_file_path

# Demonstration script execution
if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        # Navigate to practice website
        driver.get("https://testautomationpractice.blogspot.com/")

        # 1. Take full page screenshot using generic utility method
        ss1 = take_screenshot(driver, "homepage_loaded")

        # Interact with element
        name_input = driver.find_element(By.ID, "name")
        name_input.send_keys("Selenium Screenshot Demo")
        
        # 2. Take second screenshot after interaction
        ss2 = take_screenshot(driver, "after_input_entered")

        # 3. Capture specific element screenshot (Selenium 4 feature)
        header_logo = driver.find_element(By.CLASS_NAME, "titlewrapper")
        logo_path = os.path.join(os.getcwd(), "captured_screenshots", "header_logo.png")
        header_logo.save_screenshot(logo_path)
        print(f"[SUCCESS] Element screenshot captured: {logo_path}")

    finally:
        driver.quit()
        print("Driver session closed.")
