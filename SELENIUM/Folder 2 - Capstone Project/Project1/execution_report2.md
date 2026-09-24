# Test Execution Report: Capstone Project 2 - TutorialsNinja E-Commerce Automation

**Project Name:** Capstone Project 2 - TutorialsNinja E-Commerce Automation  
**Script Name:** [`Python_Automation2.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation2.py)  
**Target Website:** [TutorialsNinja Demo](https://tutorialsninja.com/demo/)  
**Browser / Driver:** Google Chrome (Selenium WebDriver)  
**Execution Status:** `PASSED`  
**Evidence Artifact:** [`cart_screenshot.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/cart_screenshot.png)  

---

## 1. Executive Summary

This execution report documents the automated end-to-end user journey test suite implemented in `Python_Automation2.py`. The automated test suite simulates a complete customer experience on the *TutorialsNinja Demo* e-commerce platform. It covers new user registration with dynamic email generation, newsletter subscription, product discovery across multiple categories (Mac, Monitors, Tablets), adding items to the shopping cart, navigating to the shopping cart overview, and capturing full visual evidence of the shopping cart status.

---

## 2. Test Execution Details & Environment

| Property | Details |
| :--- | :--- |
| **Test Automation Framework** | Python + Selenium WebDriver |
| **Locator Strategy** | XPath with dynamic locators (`By.XPATH`) |
| **Interaction Strategy** | JavaScript Executor Clicks (`execute_script("arguments[0].click();", element)`) & Scrolling (`window.scrollBy`) |
| **Browser Configuration** | Chrome WebDriver (Maximized Window) |
| **Dynamic Data Handling** | Unix timestamped email generation (`dipu_<timestamp>@gmail.com`) |

---

## 3. Test Steps & Verification Matrix

| Step # | Test Step Description | Target Locators / Actions | Expected Outcome | Execution Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Navigate to Base URL | `driver.get("https://tutorialsninja.com/demo/")` | TutorialsNinja homepage loaded | `PASS` |
| **2** | Open User Registration Form | Header User Menu (`//i[@class='fa fa-user']`) -> `Register` (`//a[normalize-space()='Register']`) | Registration form displayed | `PASS` |
| **3** | Populate Personal & Account Details | Firstname (`Dipu`), Lastname (`Das`), Telephone (`0123456789`), Password (`Dipu@123`), Confirm (`Dipu@123`) | Form fields populated accurately | `PASS` |
| **4** | Dynamic Email Generation | `f"dipu_{int(time.time())}@gmail.com"` | Unique email generated to prevent registration collision | `PASS` |
| **5** | Opt-in & Accept Privacy Policy | Newsletter opt-in (`name='newsletter'`), Agree policy (`name='agree'`), Click `Continue` | User account successfully created | `PASS` |
| **6** | Category 1: Mac Product Selection | Navigation link `Mac (1)` -> Click `Add to Cart` | Mac product added to shopping cart | `PASS` |
| **7** | Category 2: Monitors Product Selection | Navigation link `Monitors (2)` -> Click `Add to Cart` | Monitor product added to shopping cart | `PASS` |
| **8** | Category 3: Tablets Product Selection | Navigation link `Tablets` -> Click `Add to Cart` | Tablet product added to shopping cart | `PASS` |
| **9** | Shopping Cart Navigation | Header Cart Dropdown -> Click `View Cart` | Shopping cart page loaded with items | `PASS` |
| **10** | Capture Evidence Screenshot | `driver.save_screenshot(screenshot_path)` | Cart screenshot generated at `cart_screenshot.png` | `PASS` |

---

## 4. Execution Logs Summary

```text
Navigating to https://tutorialsninja.com/demo/...
Opening My Account dropdown and navigating to Register page...
Scrolling down page...
Entering registration details (Firstname, Lastname, Dynamic Email, Phone, Password)...
Selecting newsletter preference and accepting privacy policy...
Submitting registration form...
Navigating to 'Mac (1)' category and adding item to cart...
Navigating to 'Monitors (2)' category and adding item to cart...
Navigating to 'Tablets' category and adding item to cart...
Opening shopping cart dropdown and selecting 'View Cart'...
Scrolling to cart details...
Screenshot saved successfully at: D:\projects\selenium_assignment\Selenium\Folder 2 - Capstone Project\Project1\cart_screenshot.png
Execution completed successfully.
```

---

## 5. Artifact Verification

- **Shopping Cart Evidence Screenshot:** [`cart_screenshot.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/cart_screenshot.png)
- **Primary Test Automation Script:** [`Python_Automation2.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation2.py)

---
*Report generated automatically for Capstone Project 2 execution.*
