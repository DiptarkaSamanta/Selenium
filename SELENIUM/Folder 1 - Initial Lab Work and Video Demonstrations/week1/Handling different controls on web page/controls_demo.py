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
    # Open Practice Website
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

    print("=================================================================")
    print("DEMO: HANDLING DIFFERENT CONTROLS ON WEB PAGE")
    print("=================================================================")

    # ------------------------------------------------------------------
    # 1. Absolute vs Relative XPath & 2. Contains, Starts-With, Axes
    # ------------------------------------------------------------------
    print("\n--- 1 & 2. Advanced XPath Locators ---")
    
    # Relative XPath with contains()
    header = driver.find_element(By.XPATH, "//h1[contains(text(), 'Practice Page')]")
    print("Relative XPath Header Text:", header.text)

    # Relative XPath with starts-with()
    radio1_btn = driver.find_element(By.XPATH, "//input[starts-with(@value, 'radio1')]")
    print("Found Radio 1 using starts-with XPath")

    # Parent Axis
    radio_parent_div = radio1_btn.find_element(By.XPATH, "./parent::fieldset")
    print("Found Parent Fieldset Legend:", radio_parent_div.find_element(By.TAG_NAME, "legend").text)

    # Following-Sibling Axis
    checkbox_label = driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']/following-sibling::text()[1] | //label[@for='bmw']")

    # ------------------------------------------------------------------
    # 3. Handling Button
    # ------------------------------------------------------------------
    print("\n--- 3. Handling Button ---")
    open_window_btn = driver.find_element(By.XPATH, "//button[@id='openwindow']")
    print("Button Text:", open_window_btn.text)
    print("Is Button Displayed:", open_window_btn.is_displayed())
    print("Is Button Enabled:", open_window_btn.is_enabled())

    # ------------------------------------------------------------------
    # 4. Handling Input Box
    # ------------------------------------------------------------------
    print("\n--- 4. Handling Input Box ---")
    name_input = driver.find_element(By.XPATH, "//input[@id='name']")
    name_input.clear()
    name_input.send_keys("Diptarka Samanta")
    print("Input Box Entered Value:", name_input.get_attribute("value"))

    # ------------------------------------------------------------------
    # 5. Handling Checkbox
    # ------------------------------------------------------------------
    print("\n--- 5. Handling Checkbox ---")
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    print(f"Total Checkboxes found: {len(checkboxes)}")
    for index, cb in enumerate(checkboxes, start=1):
        if not cb.is_selected():
            cb.click()
            print(f"  Checkbox {index} checked -> is_selected: {cb.is_selected()}")
    time.sleep(1)

    # ------------------------------------------------------------------
    # 6. Handling Radio Button
    # ------------------------------------------------------------------
    print("\n--- 6. Handling Radio Button ---")
    radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
    if not radio2.is_selected():
        radio2.click()
    print("Radio Option 2 selected -> is_selected:", radio2.is_selected())
    time.sleep(1)

    # ------------------------------------------------------------------
    # 7. Handling Select Box (Dropdown)
    # ------------------------------------------------------------------
    print("\n--- 7. Handling Select Box ---")
    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    select = Select(dropdown_element)

    # Select by Visible Text
    select.select_by_visible_text("Option3")
    print("Selected Option by Visible Text:", select.first_selected_option.text)

    # Select by Value Attribute
    select.select_by_value("option1")
    print("Selected Option by Value Attribute:", select.first_selected_option.text)

    # Select by Index
    select.select_by_index(2)
    print("Selected Option by Index 2:", select.first_selected_option.text)

finally:
    time.sleep(2)
    driver.quit()
    print("\nDemo Completed & Browser Closed.")
