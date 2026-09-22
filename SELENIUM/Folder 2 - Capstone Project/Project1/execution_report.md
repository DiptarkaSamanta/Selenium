# Test Execution Report: Capstone Project Python Automation

**Project Name:** Capstone Project - E-Commerce Automation  
**Script Name:** [`Python_Automation.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation.py)  
**Target Website:** [Automation Exercise](https://automationexercise.com)  
**Browser / Driver:** Google Chrome (Headless/Interactive via Selenium WebDriver)  
**Execution Status:** `PASSED`  
**Evidence Artifact:** [`order_evidence.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/order_evidence.png)  

---

## 1. Executive Summary

This execution report documents the automated end-to-end user journey test suite implemented in `Python_Automation.py`. The automated test suite simulates a complete customer lifecycle on the *Automation Exercise* platform, encompassing user registration, account profile creation, product search, cart quantity modification, checkout progression, and automated visual proof generation.

---

## 2. Test Execution Details & Environment

| Property | Details |
| :--- | :--- |
| **Test Automation Framework** | Python + Selenium WebDriver |
| **Wait Strategy** | Explicit Waits (`WebDriverWait`) + Safe Click Wrappers |
| **Page Load Strategy** | Eager (`options.page_load_strategy = 'eager'`) |
| **Resolution / Window** | Maximized Window |
| **Popup Handling** | `--disable-notifications`, `--disable-popup-blocking` |

---

## 3. Test Steps & Verification Matrix

| Step # | Test Step Description | Target Locators / Actions | Expected Outcome | Execution Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Navigate to Base URL | `driver.get("https://automationexercise.com")` | Homepage loads successfully | `PASS` |
| **2** | Navigate to Signup / Login | `XPath: //a[normalize-space()='Signup / Login']` | Login / Signup page displayed | `PASS` |
| **3** | Initiate New User Registration | Name: `Dipu4`<br>Email: Dynamic timestamped email | User creation form opens | `PASS` |
| **4** | Fill Account & Address Details | Title, Password (`dipu@123`), DOB (`31/10/2004`), Newsletter opt-in, Full Address (Asansol, WB, India - `713301`) | All mandatory fields populated | `PASS` |
| **5** | Trigger Account Creation | `CSS: button[data-qa='create-account']` | Account Created confirmation | `PASS` |
| **6** | Product Catalog Navigation | Navigate to `/products` | Catalog page loaded | `PASS` |
| **7** | Search Product | Search Query: `tshirt` | Relevant product results returned | `PASS` |
| **8** | Select Product Details | `CSS: a[href='/product_details/2']` | Product details view rendered | `PASS` |
| **9** | Update Quantity & Add to Cart | Input Quantity: `4`<br>Click `Add to cart` | 4 units added to cart | `PASS` |
| **10** | Navigate to Cart & Checkout | `/view_cart` -> `.btn.btn-default.check_out` | Order summary & checkout page | `PASS` |
| **11** | Capture Order Evidence Screenshot | Save screenshot to `order_evidence.png` | `order_evidence.png` generated | `PASS` |

---

## 4. Execution Logs Summary

```text
Navigating to https://automationexercise.com...
Step 1: Clicking Signup / Login button...
Step 2: Entering Name and Email for signup...
Step 3: Filling Account Information...
Creating account...
Clicking Continue button after account creation...
Step 4: Navigating to Products...
Searching product 'tshirt'...
Selecting product details...
Step 5: Updating quantity to 4 and adding to cart...
Navigating to Cart...
Step 6: Proceeding to checkout...
SUCCESS: Screenshot saved successfully at D:\projects\selenium_assignment\Selenium\Folder 2 - Capstone Project\Project1\order_evidence.png
```

---

## 5. Artifact Verification

- **Order Evidence Screenshot:** [`order_evidence.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/order_evidence.png)
- **Primary Test Script:** [`Python_Automation.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation.py)

---
*Report generated automatically for Capstone Project execution.*
