import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os

driver = webdriver.Chrome()

try:
    # Open public practice website
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Verify page title
    print("Page title:", driver.title)

    assert driver.title == "Swag Labs"

    wait = WebDriverWait(driver, 10)

    # Element 1: Username input
    # ID is used because the username field has a unique ID.
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )
    username.send_keys("standard_user")

    # Element 2: Password input
    # ID is used because it uniquely identifies the password field.
    password = driver.find_element(
        By.ID, "password"
    )
    password.send_keys("secret_sauce")

    # Element 3: Login button
    # CSS selector is used as a second locator strategy.
    login_button = driver.find_element(
        By.CSS_SELECTOR, "input[type='submit']"
    )
    login_button.click()

    # Explicit wait:
    # Wait until the Products heading appears after login.
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    print("Login successful.")
    print("Current page:", driver.title)

    # Interact with a product button
    # CSS selector identifies the Add to Cart button.
    add_to_cart = driver.find_element(
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack"
    )
    add_to_cart.click()

    print("Product added to cart.")

    # Expected failure
    try:
        driver.find_element(By.ID, "wrong-element-id")

    except NoSuchElementException:
        print(
            "Expected failure handled: "
            "The requested element was not found."
        )

    # Save screenshot
    screenshot_path = os.path.abspath(
        "saucedemo_success.png"
    )

    driver.save_screenshot(screenshot_path)

    print("Screenshot saved at:")
    print(screenshot_path)

except TimeoutException:
    print(
        "Timeout error: The expected element "
        "did not appear within 10 seconds."
    )

except Exception as e:
    print("Unexpected error:", e)

finally:
    # Always close the browser, even if an error occurs.
    driver.quit()
    print("Browser closed safely.")

time.sleep(5)