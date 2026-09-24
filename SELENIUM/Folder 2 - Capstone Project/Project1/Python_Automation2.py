from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()

try:
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    time.sleep(3)

    account_dropdown = driver.find_element(By.XPATH, "//i[@class='fa fa-user']")
    account_dropdown.click()
    time.sleep(2)

    registration = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")
    registration.click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    firstname = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    firstname.send_keys("Dipu")
    time.sleep(2)

    lastname = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    lastname.send_keys("Das")
    time.sleep(2)

    email = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email.send_keys(f"dipu_{int(time.time())}@gmail.com")
    time.sleep(2)

    telephone = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    telephone.send_keys("0123456789")
    time.sleep(2)

    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys("Dipu@123")
    time.sleep(2)

    confirm_password = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    confirm_password.send_keys("Dipu@123")
    time.sleep(2)

    subscribe = driver.find_element(By.XPATH, "(//input[@name='newsletter'])[1]")
    subscribe.click()
    time.sleep(2)

    policy = driver.find_element(By.XPATH, "//input[@name='agree']")
    policy.click()
    time.sleep(2)

    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_button.click()
    time.sleep(2)

    mac_find = driver.find_element(By.XPATH, "//a[normalize-space()='Mac (1)']")
    driver.execute_script("arguments[0].click();", mac_find)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    addtocart_mac = driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']")
    driver.execute_script("arguments[0].click();", addtocart_mac)
    time.sleep(2)

    monitor_find = driver.find_element(By.XPATH, "//a[normalize-space()='Monitors (2)']")
    driver.execute_script("arguments[0].click();", monitor_find)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    addtocart_monitor = driver.find_element(By.XPATH, "//div[@id='product-category']//div[2]//div[1]//div[2]//div[2]//button[1]//i[1]")
    driver.execute_script("arguments[0].click();", addtocart_monitor)
    time.sleep(2)

    tablet_find = driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(),'Tablets')]")
    driver.execute_script("arguments[0].click();", tablet_find)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    addtocart_tablet = driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']")
    driver.execute_script("arguments[0].click();", addtocart_tablet)
    time.sleep(2)

    view_cart = driver.find_element(By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    driver.execute_script("arguments[0].click();", view_cart)
    time.sleep(1)
    
    view_cart = driver.find_element(By.XPATH, "//strong[normalize-space()='View Cart']")
    driver.execute_script("arguments[0].click();", view_cart)
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 220);")
    time.sleep(2)

    screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cart_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved successfully at: {screenshot_path}")
    
finally:
    driver.quit()