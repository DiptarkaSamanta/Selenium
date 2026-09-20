# =========================================================================
# SYNCHRONIZATION AND WAIT TYPES
# Website: https://practice.softwaretestingmentor.com/login
# Syllabus Covered:
# 1. Why Synchronization? (Prevents timing errors when elements load asynchronously)
# 2. Implicit wait
# 3. Explicit wait
# =========================================================================

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options to bypass Cloudflare automation checks
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

def open_url(url):
    """Safely loads URL with retry logic if connection is reset."""
    for _ in range(3):
        try:
            driver.get(url)
            time.sleep(2)
            return
        except Exception:
            time.sleep(2)

try:
    print("=================================================================")
    print("SYNCHRONIZATION AND WAIT TYPES DEMO")
    print("Website: https://practice.softwaretestingmentor.com/login")
    print("=================================================================\n")

    # -------------------------------------------------------------------------
    # 1. IMPLICIT WAIT (Global Wait)
    # -------------------------------------------------------------------------
    print("--- 1. Testing Implicit Wait ---")
    driver.implicitly_wait(10)  # Applies globally to all find_element searches

    open_url("https://practice.softwaretestingmentor.com/login")

    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("demo_user")
    print("Located and populated Username field via Implicit Wait.")

    # -------------------------------------------------------------------------
    # 2. EXPLICIT WAIT (Targeted Conditional Wait)
    # -------------------------------------------------------------------------
    print("\n--- 2. Testing Explicit Wait ---")
    driver.implicitly_wait(0)  # Reset implicit wait
    wait = WebDriverWait(driver, 10)  # Explicit wait instance with 10s timeout

    # Wait until password field is visible
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys("demo_pass123")
    print("Found Password field via Explicit Wait (visibility_of_element_located).")

    # Wait until Sign In button is clickable
    login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "login-btn"))
    )
    print(f"Found Sign In button via Explicit Wait (element_to_be_clickable). Button Text: '{login_btn.text}'")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser closed successfully.")
