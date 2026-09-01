from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

try:
    # 1. Open website and verify title
    driver.get("https://the-internet.herokuapp.com/")
    print("Title:", driver.title)

    assert driver.title == "The Internet"
    print("Title verified successfully")

    wait = WebDriverWait(driver, 10)

    # 2. Element type 1: Link
    # LINK_TEXT is used because the link has clear visible text.
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    # 3. Element type 2: Username
    # ID is used because it uniquely identifies the username field.
    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    # 4. Element type 3: Password
    driver.find_element(
        By.ID, "password"
    ).send_keys("SuperSecretPassword!")

    # 5. Login button
    # CSS_SELECTOR is used as a second locator strategy.
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # 6. Explicit wait for successful login
    wait.until(EC.url_contains("/secure"))
    print("Correct login successful")

    # 7. Logout
    # LINK_TEXT is used because Logout is a visible link.
    driver.find_element(By.LINK_TEXT, "Logout").click()
    print("Logout successful")

    # 8. Login again with WRONG password
    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys("tomsmith")

    driver.find_element(
        By.ID, "password"
    ).send_keys("wrongpassword")

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # 9. Wait for error message
    wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    print("Wrong password error displayed.")

    # Keep the error page visible for 5 seconds
    time.sleep(5)

    # 10. Expected failure
    try:
        driver.find_element(By.ID, "wrong-id")

    except NoSuchElementException:
        print("Expected failure handled: element not found.")

    # 11. Save screenshot
    driver.save_screenshot("heroku_wrong_password.png")
    print("Screenshot saved as heroku_wrong_password.png")

except Exception as e:
    print("Error:", e)

finally:
    # 12. Close browser safely
    driver.quit()
    print("Browser closed safely.")