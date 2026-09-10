from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Edge WebDriver
driver = webdriver.Edge()
driver.maximize_window()

try:
    # -------------------------------------------------------------------------
    # 1. IMPLICIT WAIT DEMO (Global Wait)
    # -------------------------------------------------------------------------
    print("--- Testing Implicit Wait ---")
    driver.implicitly_wait(10)  # Applies globally to all element searches
    
    driver.get("https://testautomationpractice.blogspot.com/")
    
    name_field = driver.find_element(By.ID, "name")
    name_field.clear()
    name_field.send_keys("Implicit Wait Test")
    print("Successfully populated name field using Implicit Wait.")

    # -------------------------------------------------------------------------
    # 2. EXPLICIT WAIT DEMO (Targeted Conditional Wait)
    # -------------------------------------------------------------------------
    print("\n--- Testing Explicit Wait ---")
    wait = WebDriverWait(driver, 10)  # Explicit wait instance with 10s timeout

    # Wait until the 'Point Me' hover button is visible
    point_me_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Point Me')]"))
    )
    print("Found 'Point Me' button via Explicit Wait.")

    # Wait until text box is clickable
    email_field = wait.until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    email_field.clear()
    email_field.send_keys("explicitwait@example.com")
    print("Successfully populated email field via Explicit Wait.")

finally:
    time.sleep(2)
    driver.quit()
    print("Driver closed successfully.")
