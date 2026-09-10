from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    print("=================================================================")
    print("DEMO: HANDLING DIFFERENT CONTROLS ON WEB PAGE - ADVANCED")
    print("=================================================================")

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

    # 1. Handling Alert Box
    print("\n--- 1. Handling Alert Box ---")
    driver.find_element(By.ID, "name").send_keys("Diptarka")
    driver.find_element(By.ID, "alertbtn").click()
    alert = driver.switch_to.alert
    print("Alert Message:", alert.text)
    time.sleep(1)
    alert.accept()

    # 2. Handling Multiple Windows / Tabs
    print("\n--- 2. Handling Multiple Windows/Tabs ---")
    parent_handle = driver.current_window_handle
    driver.find_element(By.ID, "openwindow").click()
    time.sleep(2)
    
    for handle in driver.window_handles:
        if handle != parent_handle:
            driver.switch_to.window(handle)
            print("Switched to Child Window Title:", driver.title)
            time.sleep(1)
            driver.close()
    
    driver.switch_to.window(parent_handle)
    print("Switched back to Parent Window")

    # 3. Working with Scrollbar
    print("\n--- 3. Working with Scrollbar ---")
    driver.execute_script("window.scrollBy(0, 500);")
    print("Scrolled down by 500px")
    time.sleep(1)

    mouse_hover_btn = driver.find_element(By.ID, "mousehover")
    driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_btn)
    print("Scrolled element 'mousehover' into view")
    time.sleep(1)

    # 4. Handling Iframes
    print("\n--- 4. Handling Iframes ---")
    iframe_element = driver.find_element(By.ID, "courses-iframe")
    driver.switch_to.frame(iframe_element)
    print("Switched inside iframe")
    time.sleep(1)
    
    driver.switch_to.default_content()
    print("Switched back to main page default content")

    # 5. State of Web Element (Disabled vs Enabled)
    print("\n--- 5. Element State (Enabled / Disabled) ---")
    name_field = driver.find_element(By.ID, "name")
    print("Is Name Input Displayed:", name_field.is_displayed())
    print("Is Name Input Enabled:", name_field.is_enabled())

    # 6. Get Text & Attribute Values
    print("\n--- 6. Get Text & Attribute Value ---")
    legend_text = driver.find_element(By.XPATH, "//fieldset/legend[text()='Dropdown Example']").text
    print("Legend Text:", legend_text)
    
    name_field.clear()
    name_field.send_keys("Test Attribute")
    attr_val = name_field.get_attribute("value")
    print("Input Value Attribute:", attr_val)

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser Session Closed Successfully.")
