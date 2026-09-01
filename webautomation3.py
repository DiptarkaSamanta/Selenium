from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/")

    # Verify title
    assert driver.title == "The Internet"
    print("Title verified")

    # Link
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()

    # Username and password
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Explicit wait
    WebDriverWait(driver, 10).until(
        lambda d: "/secure" in d.current_url
    )
    print("Login successful")

    # Logout
    driver.find_element(By.LINK_TEXT, "Logout").click()

    # Wrong password
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)

    # Expected failure
    try:
        driver.find_element(By.ID, "wrong-id")
    except Exception:
        print("Expected failure handled")

    # Screenshot
    driver.save_screenshot("heroku_wrong_password.png")
    print("Screenshot saved")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()