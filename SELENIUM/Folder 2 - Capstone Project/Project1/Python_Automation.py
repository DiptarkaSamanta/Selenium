from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

driver = webdriver.Chrome()

try:
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    time.sleep(3)

    # Step 1: Click Signup / Login
    signup_login = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    signup_login.click()
    time.sleep(2)

    # Step 2: New User Signup
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    name_input.send_keys("Dipu")
    time.sleep(1)

    signup_email = f"dipu_{int(time.time())}@gmail.com"
    email_input = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    email_input.send_keys(signup_email)
    time.sleep(1)

    signup_btn = driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
    signup_btn.click()
    time.sleep(2)

    # Step 3: Fill Account Information
    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(1)

    gender_radio = driver.find_element(By.XPATH, "//input[@id='id_gender1']")
    gender_radio.click()
    time.sleep(1)

    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input.send_keys("Dipu@123")
    time.sleep(1)

    day_select = Select(driver.find_element(By.XPATH, "//select[@id='days']"))
    day_select.select_by_value("31")

    month_select = Select(driver.find_element(By.XPATH, "//select[@id='months']"))
    month_select.select_by_value("10")

    year_select = Select(driver.find_element(By.XPATH, "//select[@id='years']"))
    year_select.select_by_value("2004")
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(1)

    newsletter_cb = driver.find_element(By.XPATH, "//input[@id='newsletter']")
    driver.execute_script("arguments[0].click();", newsletter_cb)

    optin_cb = driver.find_element(By.XPATH, "//input[@id='optin']")
    driver.execute_script("arguments[0].click();", optin_cb)
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Dipu")
    driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Das")
    driver.find_element(By.XPATH, "//input[@id='company']").send_keys("Nvidia")
    driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("12, AB block")
    driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("34, CD block")

    country_select = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
    country_select.select_by_value("India")

    driver.find_element(By.XPATH, "//input[@id='state']").send_keys("West Bengal")
    driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Asansol")
    driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("713301")
    driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("0123456789")
    time.sleep(1)

    create_acc_btn = driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
    driver.execute_script("arguments[0].click();", create_acc_btn)
    time.sleep(2)

    continue_btn = driver.find_element(By.XPATH, "//a[@data-qa='continue-button']")
    driver.execute_script("arguments[0].click();", continue_btn)
    time.sleep(2)

    # Step 4: Search & Select Product
    products_link = driver.find_element(By.XPATH, "//a[@href='/products']")
    driver.execute_script("arguments[0].click();", products_link)
    time.sleep(2)

    search_input = driver.find_element(By.XPATH, "//input[@id='search_product']")
    search_input.send_keys("tshirt")
    search_btn = driver.find_element(By.XPATH, "//button[@id='submit_search']")
    search_btn.click()
    time.sleep(2)

    view_product = driver.find_element(By.XPATH, "//a[@href='/product_details/2']")
    driver.execute_script("arguments[0].click();", view_product)
    time.sleep(2)

    # Step 5: Update quantity and Add to cart
    quantity_input = driver.find_element(By.XPATH, "//input[@id='quantity']")
    quantity_input.clear()
    quantity_input.send_keys("4")
    time.sleep(1)

    add_to_cart = driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
    add_to_cart.click()
    time.sleep(2)

    view_cart = driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']")
    driver.execute_script("arguments[0].click();", view_cart)
    time.sleep(2)

    # Step 6: Proceed to checkout & Save Screenshot
    checkout_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    driver.execute_script("arguments[0].click();", checkout_btn)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "order_evidence.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved successfully at: {screenshot_path}")

finally:
    driver.quit()
