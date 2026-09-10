from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    # Open Practice Page
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

    # 1. Radio Button Handling
    print("--- 1. Radio Buttons ---")
    radio_button = driver.find_element(By.XPATH, "//input[@value='radio1']")
    radio_button.click()
    print("Radio Button 1 Selected:", radio_button.is_selected())
    time.sleep(1)

    # 2. Static Dropdown (Select Class)
    print("\n--- 2. Dropdown Selection ---")
    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    select = Select(dropdown_element)
    select.select_by_visible_text("Option2")
    print("Selected Option 2 via Select class")
    time.sleep(1)

    # 3. Checkboxes Handling
    print("\n--- 3. Checkboxes ---")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for index, checkbox in enumerate(checkboxes, start=1):
        if not checkbox.is_selected():
            checkbox.click()
            print(f"Checkbox {index} checked")
    time.sleep(1)

    # 4. Dynamic Auto-Suggest Dropdown
    print("\n--- 4. Auto-Suggest Input ---")
    autocomplete_input = driver.find_element(By.ID, "autocomplete")
    autocomplete_input.send_keys("Germany")
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[text()='Germany']").click()
    print("Selected 'Germany' from auto-suggest dropdown")
    time.sleep(1)

    # 5. Alert / Popup Handling
    print("\n--- 5. Web Alert Handling ---")
    name_box = driver.find_element(By.ID, "name")
    name_box.send_keys("Diptarka")
    
    alert_btn = driver.find_element(By.ID, "alertbtn")
    alert_btn.click()
    
    alert_popup = driver.switch_to.alert
    print("Alert Message Received:", alert_popup.text)
    time.sleep(2)
    alert_popup.accept()
    print("Alert Accepted successfully")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser closed successfully.")
