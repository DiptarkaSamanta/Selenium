from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import traceback

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

def safe_click(by, value):
    el = wait.until(EC.presence_of_element_located((by, value)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
    time.sleep(0.5)
    try:
        driver.execute_script("arguments[0].click();", el)
    except Exception:
        el.click()
    return el

def send_keys_el(by, value, keys):
    el = wait.until(EC.presence_of_element_located((by, value)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
    time.sleep(0.3)
    el.clear()
    el.send_keys(keys)
    return el

try:
    print("Navigating to https://automationexercise.com...")
    driver.get("https://automationexercise.com")
    time.sleep(2)

    # Step 1: Click Signup / Login
    print("Step 1: Clicking Signup / Login button...")
    safe_click(By.XPATH, "//a[normalize-space()='Signup / Login']")
    time.sleep(2)

    # Step 2: New User Signup
    print("Step 2: Entering Name and Email for signup...")
    send_keys_el(By.XPATH, "//input[@placeholder='Name']", "Dipu4")

    signup_email = f"Dipu_{int(time.time())}@gmail.com"
    send_keys_el(By.XPATH, "//input[@data-qa='signup-email']", signup_email)
    time.sleep(1)

    safe_click(By.CSS_SELECTOR, "button[data-qa='signup-button']") 
    time.sleep(2) 

    # Step 3: Fill Account Information
    print("Step 3: Filling Account Information...")
    safe_click(By.ID, "id_gender1")
    send_keys_el(By.ID, "password", "dipu@123")
    time.sleep(1)

    day_element = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='days']")))
    Select(day_element).select_by_value("31")

    month_element = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='months']")))
    Select(month_element).select_by_value("10")

    year_element = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='years']")))
    Select(year_element).select_by_value("2004")
    time.sleep(1)

    safe_click(By.XPATH, "//label[@for='newsletter']")
    safe_click(By.XPATH, "//input[@id='optin']")
    time.sleep(1)

    send_keys_el(By.ID, "first_name", "Dipu")
    send_keys_el(By.ID, "last_name", "Das")
    send_keys_el(By.XPATH, "//input[@name='company']", "Nvida")
    send_keys_el(By.ID, "address1", "12, AB block")
    send_keys_el(By.ID, "address2", "34, CD block")

    country_element = wait.until(EC.presence_of_element_located((By.ID, "country")))
    Select(country_element).select_by_value("India")

    send_keys_el(By.ID, "state", "West Bengal")
    send_keys_el(By.ID, "city", "Asansol")
    send_keys_el(By.ID, "zipcode", "713301")
    send_keys_el(By.ID, "mobile_number", "0123456789")
    time.sleep(1)

    print("Creating account...")
    safe_click(By.CSS_SELECTOR, "button[data-qa='create-account']")
    time.sleep(2)

    print("Clicking Continue button after account creation...")
    try:
        safe_click(By.CSS_SELECTOR, "a[data-qa='continue-button']")
        time.sleep(2)
    except Exception as e:
        print(f"Continue button note: {e}")

    # Step 4: Search & Select Product
    print("Step 4: Navigating to Products...")
    driver.get("https://automationexercise.com/products")
    time.sleep(2)

    print("Searching product 'tshirt'...")
    send_keys_el(By.ID, "search_product", "tshirt")
    safe_click(By.ID, "submit_search")
    time.sleep(2)

    print("Selecting product details...")
    safe_click(By.CSS_SELECTOR, "a[href='/product_details/2']")
    time.sleep(2)

    # Step 5: Update quantity and Add to cart
    print("Step 5: Updating quantity to 4 and adding to cart...")
    send_keys_el(By.ID, "quantity", "4")
    safe_click(By.XPATH, "//button[normalize-space()='Add to cart']")
    time.sleep(2)

    print("Navigating to Cart...")
    driver.get("https://automationexercise.com/view_cart")
    time.sleep(2)

    # Step 6: Proceed to checkout
    print("Step 6: Proceeding to checkout...")
    safe_click(By.CSS_SELECTOR, ".btn.btn-default.check_out")
    time.sleep(2)

    actions.scroll_by_amount(0, 200).perform()
    time.sleep(1)

    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "order_evidence.png")
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    driver.get_screenshot_as_file(screenshot_path)
    print(f"SUCCESS: Screenshot saved successfully at {screenshot_path}")

    actions.scroll_by_amount(0, 200).perform()
    time.sleep(3)

except Exception as e:
    print(f"An error occurred during execution: {e}")
    traceback.print_exc()

finally:
    driver.quit()


