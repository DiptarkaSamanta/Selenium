"""
Locators and Object Identification Demonstration Script
Selenium 4 in Python

Topics Covered:
1. Identifying elements by ID and Name
2. Locating by Tag Name, Link Text, Class Name
3. Finding List of Elements (find_elements)
4. CSS Selectors: Basic, Wildcards (^=, $=, *=), and Child Nodes / Pseudo-classes
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run_locators_demo():
    # Initialize Chrome WebDriver using Selenium 4 native driver management
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        print("=== 1. Find Element by ID and NAME ===")
        driver.get("https://testautomationpractice.blogspot.com/")
        
        # Locating by ID
        name_field = driver.find_element(By.ID, "name")
        name_field.clear()
        name_field.send_keys("John Doe")
        print("Successfully populated element found by ID ('name').")

        # Locating by Name (using another form field or text area if present)
        # Note: 'phone' or 'email' input elements can also be targeted by Name if present
        email_field = driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys("johndoe@example.com")

        print("\n=== 2. Locating by Tag Name, Link Text, Class Name ===")
        # Locating by Tag Name
        page_headers = driver.find_elements(By.TAG_NAME, "h1")
        for header in page_headers:
            print(f"Header Tag (h1) text: '{header.text}'")

        # Locating by Link Text
        try:
            home_link = driver.find_element(By.LINK_TEXT, "Home")
            print(f"Found Link Text 'Home' with href: {home_link.get_attribute('href')}")
        except Exception as e:
            print("Link Text 'Home' check complete.")

        # Locating by Class Name
        # Note: Class name must be a single class string (e.g. 'title')
        title_element = driver.find_element(By.CLASS_NAME, "title")
        print(f"Element located by Class Name 'title': '{title_element.text}'")

        print("\n=== 3. Find List of Elements (find_elements) ===")
        # Finding all input elements of type text/checkbox/radio
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Total <input> elements found on page: {len(all_inputs)}")

        # Finding list of options in country dropdown or checkboxes
        days_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"Total Checkboxes found: {len(days_checkboxes)}")
        for idx, checkbox in enumerate(days_checkboxes, start=1):
            val = checkbox.get_attribute("id") or checkbox.get_attribute("value")
            print(f" Checkbox #{idx} ID/Value: {val}")

        print("\n=== 4. CSS Selectors: Wildcards and Child Nodes ===")
        
        # Standard CSS: ID (#) and Class (.)
        css_by_id = driver.find_element(By.CSS_SELECTOR, "#phone")
        css_by_id.clear()
        css_by_id.send_keys("9876543210")
        print("CSS Selector by ID (#phone) working.")

        # Wildcard 1: Starts with (^=)
        # Matches any input whose ID starts with 'txt' or 'date'
        css_starts_with = driver.find_element(By.CSS_SELECTOR, "input[id^='name']")
        print(f"CSS Wildcard Starts-with (^=): Found element ID '{css_starts_with.get_attribute('id')}'")

        # Wildcard 2: Ends with ($=)
        css_ends_with = driver.find_element(By.CSS_SELECTOR, "textarea[id$='area']")
        css_ends_with.clear()
        css_ends_with.send_keys("123 Automation St, Tech City")
        print("CSS Wildcard Ends-with ($=): Populated textarea ending with 'area'.")

        # Wildcard 3: Contains (*=)
        css_contains = driver.find_element(By.CSS_SELECTOR, "input[id*='phon']")
        print(f"CSS Wildcard Contains (*=): Found element with ID containing 'phon': '{css_contains.get_attribute('id')}'")

        # Child Node Traversal (> direct child, space descendant, :nth-child)
        # Direct Child Selector
        direct_child = driver.find_element(By.CSS_SELECTOR, "div.form-group > label[for='name']")
        print(f"Direct Child Selector (div.form-group > label): '{direct_child.text}'")

        # Nth-Child Positional Selector
        # Targeting specific rows or table cells
        table_cell = driver.find_element(By.CSS_SELECTOR, "table[name='BookTable'] tr:nth-child(2) > td:nth-child(1)")
        print(f"Nth-Child Selector (BookTable tr:nth-child(2) > td:nth-child(1)): Cell text = '{table_cell.text}'")

        time.sleep(2)
        print("\nLocators and Object Identification Demonstration Completed Successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_locators_demo()
