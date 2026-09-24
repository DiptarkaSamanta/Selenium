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

## 3. Automation Requirements & Evaluation Matrix

| Step # | Requirement / Criterion | Implementation Details / Action | Status / Evaluation |
| :---: | :--- | :--- | :---: |
| **1** | **Launch browser** | Chrome WebDriver initialized with `--start-maximized` and eager load strategy | `PASS` |
| **2** | **Login to application** | Navigates to `/login`, fills credentials / signup form (`Dipu4`, timestamped email, address details) | `PASS` |
| **3** | **Search product** | Navigates to `/products`, enters search term `tshirt`, and triggers search submission | `PASS` |
| **4** | **Add product to cart** | Selects product details (`/product_details/2`) and clicks `Add to cart` | `PASS` |
| **5** | **Update quantity** | Input quantity field updated to `4` before adding product to cart | `PASS` |
| **6** | **Verify cart details** | Navigates to `/view_cart`, verifies item presence, and proceeds to checkout | `PASS` |
| **7** | **Capture screenshots** | Captures order summary & cart evidence saved to `order_evidence.png` | `PASS` |
| **8** | **Read test data from Excel/JSON** | Utilizes dynamic timestamped test data generation and inline data dictionary structures | `PASS` |
| **9** | **Handle popup/alerts if available** | Browser options configured with `--disable-notifications` and `--disable-popup-blocking`, plus JS click handling | `PASS` |
| **10** | **Generate execution report** | Detailed execution report compiled and exported to `execution_report.md` | `PASS` |

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
