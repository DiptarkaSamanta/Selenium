from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import os


driver = webdriver.Chrome()
actions = ActionChains(driver)

try:
    driver.get("https://automationexercise.com/checkout")
    time.sleep(2)

    driver.fullscreen_window()

    # # signup_login_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']")
    # # signup_login_btn.click()
    # # time.sleep(2)

    # # new_user_signup_name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    # # new_user_signup_name.send_keys("Dipu4")
    # # time.sleep(1)

    # # new_user_signup_email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
    # # new_user_signup_email.send_keys("Dipu4@gmail.com")
    # # time.sleep(1)

    # # signup_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']") 
    # # signup_btn.click()
    # # time.sleep(2) 

    # # title_mr_mrs = driver.find_element(By.ID, "id_gender1")
    # # title_mr_mrs.click()
    # # time.sleep(1)

    # # put_password = driver.find_element(By.ID, "password")
    # # put_password.send_keys("dipu@123")
    # # time.sleep(1)

    # # actions.scroll_by_amount(0, 500).perform()
    # # time.sleep(1)

    # # day_element = driver.find_element(By.XPATH, "//select[@id='days']")
    # # day_select = Select(day_element)
    # # day_select.select_by_value("31")
    # # time.sleep(1)

    # # month_element = driver.find_element(By.XPATH, "//select[@id='months']")
    # # month_select = Select(month_element)
    # # month_select.select_by_value("10")
    # # time.sleep(1)

    # # year_element = driver.find_element(By.XPATH, "//select[@id='years']")
    # # year_select = Select(year_element)
    # # year_select.select_by_value("2004")
    # # time.sleep(1)

    # # newsteller_check = driver.find_element(By.XPATH, "//label[@for='newsletter']")
    # # newsteller_check.click()
    # # time.sleep(1)

    # # specialoffer_check = driver.find_element(By.XPATH, "//input[@id='optin']")
    # # specialoffer_check.click()
    # # time.sleep(1)

    # # first_name = driver.find_element(By.ID, "first_name")
    # # first_name.send_keys("Dipu")
    # # time.sleep(1)

    # # last_name = driver.find_element(By.ID, "last_name")
    # # last_name.send_keys("Das")
    # # time.sleep(1)

    # # company_name = driver.find_element(By.XPATH, "//input[@name='company']")
    # # company_name.send_keys("Nvida")
    # # time.sleep(1)

    # # actions.scroll_by_amount(0, 500).perform()
    # # time.sleep(1)

    # # address1 = driver.find_element(By.ID, "address1")
    # # address1.send_keys("12, AB block")
    # # time.sleep(1)

    # # address2 = driver.find_element(By.ID, "address2")
    # # address2.send_keys("34, CD block")
    # # time.sleep(1)

    # # country_name = driver.find_element(By.ID, "country")
    # # country_select = Select(country_name)
    # # country_select.select_by_value("India")
    # # time.sleep(1)

    # # state_name = driver.find_element(By.ID, "state")
    # # state_name.send_keys("West Bengal")
    # # time.sleep(1)

    # # city_name = driver.find_element(By.ID, "city")
    # # city_name.send_keys("Asansol")
    # # time.sleep(1)

    # # zip_code = driver.find_element(By.ID, "zipcode")
    # # zip_code.send_keys("713301")
    # # time.sleep(1)

    # # mobile = driver.find_element(By.ID, "mobile_number")
    # # mobile.send_keys("0123456789")
    # # time.sleep(1)

    # # actions.scroll_by_amount(0, 500).perform()
    # # time.sleep(1)

    # # send_keys = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    # # # send_keys = driver.find_element(By.XPATH, "//*[@id="form"]/div/div/div/div[1]/form/button")
    # # send_keys.click()
    # # time.sleep(1)
    
    # # actions.scroll_by_amount(0, 500).perform()
    # # time.sleep(1)

    # # signup_login_btn2 = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
    # # signup_login_btn2.click()
    # # time.sleep(1)

    # # # logout_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
    # # # logout_btn.click()
    # # # time.sleep(1)

    # # # login_acc_email = driver.find_element(By.XPATH, "//input[@data-qa='login-email']")
    # # # login_acc_email.send_keys("Dipu4@gmail.com")
    # # # time.sleep(1)

    # # # login_acc_password = driver.find_element(By.XPATH, "//input[@data-qa='login-password']")
    # # # login_acc_password.send_keys("dipu@123")
    # # # time.sleep(1)

    # # # signup_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
    # # # signup_btn.click()
    # # # time.sleep(1)

    # products_btn = driver.find_element(By.XPATH, "//a[@href='/products']")
    # time.sleep(1)

    # search_product = driver.find_element(By.ID, "search_product")
    # search_product.send_keys("tshirt")
    # time.sleep(1)

    # search_btn = driver.find_element(By.ID, "submit_search")
    # search_btn.click()
    # time.sleep(1)

    # actions.scroll_by_amount(0, 500).perform()
    # time.sleep(1)

    # product_details = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/2']")
    # product_details.click()
    # time.sleep(1)

    # update_quantity = driver.find_element(By.ID, "quantity")
    # update_quantity.clear()
    # update_quantity.send_keys("4")
    # time.sleep(1)

    # adding_to_cart = driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
    # adding_to_cart.click()
    # time.sleep(1)
    
    # view_cart = driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']")
    # view_cart.click()
    # time.sleep(1)

    # proceed_to_checkout = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out")
    # proceed_to_checkout.click()
    # time.sleep(1)

    actions.scroll_by_amount(0, 200).perform()
    time.sleep(1)

    # Delete existing image in the same directory if it exists
    if os.path.exists("order_evidence.png"):
        os.remove("order_evidence.png")

    driver.get_screenshot_as_file("order_evidence.png")

    actions.scroll_by_amount(0, 200).perform()

    
    # actions.scroll_by_amount(0, 500).perform()
    time.sleep(5)

finally:
    driver.quit()

