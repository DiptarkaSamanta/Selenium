# 🚀 Capstone Assignment 2: Selenium Python Automation Framework

![Framework Architecture](https://img.shields.io/badge/Architecture-Page_Object_Model_(POM)-blue)
![Test Framework](https://img.shields.io/badge/Test_Framework-Unittest_%7C_PyTest-green)
![Language](https://img.shields.io/badge/Language-Python_3.14-blue)
![Reporting](https://img.shields.io/badge/Reporting-Pytest_HTML_Report-orange)

## 📌 Executive Overview

This repository contains **Capstone Assignment 2**, a production-ready, highly scalable **Selenium Python Test Automation Framework**. The framework automates the **Login** and **Product Search** functionalities of the e-commerce web application ([TutorialsNinja Demo](https://tutorialsninja.com/demo/)) following enterprise design patterns and best practices.

### 🌟 Key Features
- **Dual Test Runner Support**: Natively compatible with both **PyTest** and Python **Unittest** standard library.
- **Page Object Model (POM)**: Complete separation of page locators, actions, and test scripts for maximum maintainability.
- **Data-Driven Testing (CSV)**: Parameterized test execution using external CSV datasets (`login_data.csv`, `search_data.csv`).
- **Configuration Management**: Centralized settings management via `config/config.ini` and `ConfigReader`.
- **Browser & Driver Management**: Dynamic `DriverFactory` supporting Chrome, Firefox, Edge, and Headless execution modes.
- **Automated Failure Screenshots**: Automatic screenshot capture on test failure and key verification steps via `ScreenshotUtility` & `conftest.py` hooks.
- **Interactive HTML Reporting**: Rich HTML reports generated via `pytest-html` plugin (`reports/pytest_report.html`).

---

## 📂 Framework Directory Structure

```text
Project2/
│
├── config/
│   ├── config.ini                   # Configuration file (URLs, Browser options, Timeouts, Paths)
│   └── config_reader.py             # Utility class to parse and load options from config.ini
│
├── test_data/
│   ├── login_data.csv               # CSV test dataset for Login scenarios (invalid & valid credentials)
│   └── search_data.csv              # CSV test dataset for Product Search scenarios (keywords & expected results)
│
├── utilities/
│   ├── __init__.py
│   ├── driver_factory.py            # Utility for initializing WebDriver (Chrome/Firefox/Edge/Headless)
│   ├── csv_reader.py                # CSV file parser helper utility class
│   └── screenshot_utility.py        # Utility class for timestamped screenshot capture
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py                 # Parent POM class providing explicit waits, click, send_keys, screenshot
│   ├── home_page.py                 # POM class for Header, Navigation, Account Menu & Search input
│   ├── login_page.py                # POM class for Login form inputs, login button & warning alert
│   ├── account_page.py              # POM class for User Account dashboard verification
│   └── search_results_page.py       # POM class for Search results header, product titles & empty result alert
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py                # Test cases for Login functionality (Unittest + PyTest + POM + CSV)
│   └── test_search.py               # Test cases for Search functionality (Unittest + PyTest + POM + CSV)
│
├── reports/                         # Generated HTML execution reports directory
├── screenshots/                     # Automated failure and evidence screenshot capture directory
│
├── conftest.py                      # Pytest fixtures, driver management, and HTML report screenshot hooks
├── run_tests.py                     # Command-line test suite runner (supports --runner pytest/unittest)
├── pytest.ini                       # Pytest settings and marker configuration
├── requirements.txt                 # Framework Python dependencies
├── README.md                        # Comprehensive framework documentation
└── execution_report.md              # Detailed test execution summary and verification report
```

---

## 🛠️ Prerequisites & Installation

1. **Python 3.10+** (Tested on Python 3.14)
2. **Google Chrome Browser** (or Firefox / Edge)
3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration Management (`config/config.ini`)

All framework parameters are controlled via `config/config.ini`:

```ini
[DEFAULT]
base_url = https://tutorialsninja.com/demo/
browser = chrome
headless = true
implicit_wait = 10
explicit_wait = 15
screenshot_dir = screenshots
reports_dir = reports
```

To run in headed mode, change `headless = false`.

---

## 📊 Test Data Files (CSV Data-Driven)

### `test_data/login_data.csv`
| scenario | email | password | expected_result |
| :--- | :--- | :--- | :--- |
| invalid_email | invalid_user_99999@testdomain.com | WrongPass123 | failure |
| invalid_password | test_valid_user@gmail.com | InvalidPassword99 | failure |
| empty_credentials | | | failure |
| valid_login | demo_autotest_user@gmail.com | TestPassword123 | success |

### `test_data/search_data.csv`
| scenario | search_keyword | expected_outcome | expected_product_or_msg |
| :--- | :--- | :--- | :--- |
| existing_mac | MacBook | found | MacBook |
| existing_iphone | iPhone | found | iPhone |
| existing_palm | Palm Treo | found | Palm Treo Pro |
| non_existing_product | XYZNonExistentItem999 | not_found | There is no product that matches the search criteria. |

---

## 🚀 Execution Instructions

You can execute the test suite using the unified CLI runner `run_tests.py` or standard `pytest` / `unittest` commands.

### Option 1: Execute via PyTest Runner (Recommended)
Generates `reports/pytest_report.html`:
```bash
python run_tests.py --runner pytest
```
Or directly via `pytest`:
```bash
pytest -v --html=reports/pytest_report.html --self-contained-html
```

### Option 2: Execute via Unittest Discovery Runner
```bash
python run_tests.py --runner unittest
```
Or directly via standard Python `unittest`:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📈 HTML Report & Screenshot Evidence

- **HTML Report Location**: [`reports/pytest_report.html`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/reports/pytest_report.html)
- **Screenshots Directory**: [`screenshots/`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/screenshots/)
- **Detailed Execution Summary**: See [`execution_report.md`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/execution_report.md)
