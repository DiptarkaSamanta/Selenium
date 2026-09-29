# 📊 Test Execution Report - Capstone Project 2

**Project Name**: E-Commerce Selenium Automation Framework Development  
**Target Application**: [TutorialsNinja Demo](https://tutorialsninja.com/demo/)  
**Execution Date**: September 25, 2026  
**Environment**: Windows 11 | Python 3.14.7 | Chrome Headless | Selenium 4.47.0  

---

## 📌 Executive Summary

| Total Test Cases | Passed | Failed | Errors | Success Rate | Execution Mode |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **5** | **5** | **0** | **0** | **100%** | Headless Chrome (Pytest + Unittest) |

All 5 core test cases passed successfully across both Pytest and Unittest execution engines.

---

## 📋 Detailed Test Scenarios & Results

| Test ID | Test Scenario | Input Data Source | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `TC_LOG_01` | Invalid Login Iterations | `test_data/login_data.csv` (3 rows) | Warning alert `Warning: No match for E-Mail Address...` displayed | Alert displayed for all invalid credentials | **PASS** |
| `TC_LOG_02` | Login Page Navigation | Direct UI Navigation | Page Title equals `Account Login` | Page Title verified: `Account Login` | **PASS** |
| `TC_SCH_01` | Valid Product Search | `test_data/search_data.csv` (`MacBook`, `iPhone`, `Palm Treo`) | Search results header displayed & matching products present | `MacBook`, `iPhone`, `Palm Treo Pro` displayed | **PASS** |
| `TC_SCH_02` | Non-Existing Product Search | `test_data/search_data.csv` (`XYZNonExistentItem999`) | Message `There is no product that matches the search criteria.` displayed | Message verified exact match | **PASS** |
| `TC_SCH_03` | Search Title & Header Verification | Direct Search Query (`Mac`) | Page Title contains `Search - Mac` | Page Title verified: `Search - Mac` | **PASS** |

---

## 📷 Captured Evidence & Screenshot Artifacts

All test runs captured timestamped visual evidence screenshots stored in `Project2/screenshots/`:

1. **Invalid Login Evidence**:
   - [`EVIDENCE_invalid_login_invalid_email`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_invalid_login_invalid_email_20260925_145207.png)
   - [`EVIDENCE_invalid_login_invalid_password`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_invalid_login_invalid_password_20260925_145224.png)
   - [`EVIDENCE_invalid_login_empty_credentials`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_invalid_login_empty_credentials_20260925_145241.png)

2. **Login Page Navigation**:
   - [`EVIDENCE_login_page_navigation`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_login_page_navigation_20260925_145300.png)

3. **Product Search Evidence**:
   - [`EVIDENCE_search_MacBook`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_search_MacBook_20260925_145305.png)
   - [`EVIDENCE_search_iPhone`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_search_iPhone_20260925_145306.png)
   - [`EVIDENCE_search_Palm_Treo`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_search_Palm_Treo_20260925_145307.png)
   - [`EVIDENCE_search_non_existing_XYZNonExistentItem999`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_search_non_existing_XYZNonExistentItem999_20260925_145318.png)
   - [`EVIDENCE_search_header_and_title`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/EVIDENCE_search_header_and_title_20260925_145313.png)

---

## 📑 Interactive HTML Report

- Interactive PyTest HTML Execution Report: [`reports/pytest_report.html`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/reports/pytest_report.html)
