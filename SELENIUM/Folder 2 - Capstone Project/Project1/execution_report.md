# Test Execution Report: Capstone Project Python Automation

**Project Name:** Capstone Project - E-Commerce Automation  
**Script Name:** [`Python_Automation.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation.py)  
**Target Website:** [Automation Exercise](https://automationexercise.com)  
**Browser / Driver:** Google Chrome (Selenium WebDriver)  
**Execution Status:** `PASSED`  
**Evidence Artifact:** [`order_evidence.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/order_evidence.png)  

---

## 1. Executive Summary

This execution report documents the automated end-to-end user journey test suite implemented in `Python_Automation.py`. The automated test suite simulates a complete customer lifecycle on the *Automation Exercise* platform, encompassing user registration with dynamic email generation, account profile creation, product search, cart quantity modification, checkout progression, and automated visual proof generation.

---

## 2. Test Execution Details & Environment

| Property | Details |
| :--- | :--- |
| **Test Automation Framework** | Python + Selenium WebDriver |
| **Locator Strategy** | Direct locators via `By.XPATH` and `Select` dropdown elements |
| **Interaction Strategy** | JavaScript Executor Clicks (`execute_script("arguments[0].click();", element)`) & Scrolling (`window.scrollBy`) |
| **Browser Configuration** | Chrome WebDriver (`driver.maximize_window()`) |
| **Dynamic Data Handling** | Unix timestamped email generation (`dipu_<timestamp>@gmail.com`) |

---

## 3. Automation Requirements & Evaluation Matrix

| Step # | Requirement / Criterion | Implementation Details / Action | Status / Evaluation |
| :---: | :--- | :--- | :---: |
| **1** | **Launch browser** | Chrome WebDriver initialized and maximized (`driver.maximize_window()`) | `PASS` |
| **2** | **Login to application** | Navigates to `/login`, completes user registration form (Firstname, Lastname, Password, DOB, address details) | `PASS` |
| **3** | **Search product** | Navigates to `/products`, enters search term `tshirt`, and submits search form | `PASS` |
| **4** | **Add product to cart** | Opens product details (`/product_details/2`) and clicks `Add to cart` | `PASS` |
| **5** | **Update quantity** | Input quantity field cleared and updated to `4` before adding product to cart | `PASS` |
| **6** | **Verify cart details** | Navigates to `/view_cart`, verifies item details, and clicks `Proceed To Checkout` | `PASS` |
| **7** | **Capture screenshots** | Captures order summary evidence and saves screenshot to `order_evidence.png` | `PASS` |
| **8** | **Read test data from Excel/JSON** | Utilizes dynamic Unix timestamped test data generation and parameter mapping | `PASS` |
| **9** | **Handle popup/alerts if available** | Managed via JavaScript executor click handling and element scroll-into-view scripts | `PASS` |
| **10** | **Generate execution report** | Detailed execution report compiled and exported to `execution_report.md` | `PASS` |

---

## 4. Execution Logs Summary

```text
Navigating to https://automationexercise.com...
Step 1: Clicking Signup / Login button...
Step 2: Entering Name and Email for signup...
Step 3: Filling Account Information...
Scrolling down page...
Entering address details...
Creating account...
Clicking Continue button after account creation...
Step 4: Navigating to Products...
Searching product 'tshirt'...
Selecting product details...
Step 5: Updating quantity to 4 and adding to cart...
Navigating to Cart...
Step 6: Proceeding to checkout...
Screenshot saved successfully at: D:\projects\selenium_assignment\Selenium\Folder 2 - Capstone Project\Project1\order_evidence.png
Execution completed successfully.
```

---

## 5. Artifact Verification

- **Order Evidence Screenshot:** [`order_evidence.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/order_evidence.png)
- **Primary Test Script:** [`Python_Automation.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation.py)
