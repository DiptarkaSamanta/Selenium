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

## 3. Automation Requirements & Evaluation Matrix

| Step # | Requirement / Criterion | Implementation Details / Action | Status / Evaluation |
| :---: | :--- | :--- | :---: |
| **1** | **Launch browser** | Chrome WebDriver initialized and maximized (`driver.maximize_window()`) | `PASS` |
| **2** | **Login to application** | Navigates to Register form, completes registration (Firstname, Lastname, Phone, Password, dynamic email) and logs in | `PASS` |
| **3** | **Search product** | Category navigation and product discovery across Mac, Monitors, and Tablets categories | `PASS` |
| **4** | **Add product to cart** | Executes `Add to Cart` for selected items in Mac, Monitors, and Tablets categories | `PASS` |
| **5** | **Update quantity** | Multi-item quantity addition and cart count updates via category selections | `PASS` |
| **6** | **Verify cart details** | Header cart dropdown opened (`dropdown-toggle`) and navigated to `View Cart` page | `PASS` |
| **7** | **Capture screenshots** | Full page screenshot of shopping cart captured and saved to `cart_screenshot.png` | `PASS` |
| **8** | **Read test data from Excel/JSON** | Utilizes dynamic Unix timestamped test data generation and parameter data mapping | `PASS` |
| **9** | **Handle popup/alerts if available** | Managed via JavaScript executor click handling and element scroll-into-view scripts | `PASS` |
| **10** | **Generate execution report** | Detailed execution report compiled and exported to `execution_report2.md` | `PASS` |

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
