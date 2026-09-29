# 🚀 Folder 2: Capstone Project

This folder contains the complete Capstone Project source code, framework implementations, detailed execution reports, visual evidence artifacts, and video demonstration links for the e-commerce web automation projects.

---

## 📌 Project 1: E-Commerce Web Automation

This Capstone Project demonstrates end-to-end web test automation across two target e-commerce platforms to showcase comprehensive testing capabilities.

### 🌐 Website 1: Automation Exercise (`https://automationexercise.com`)
* **Target Website**: [Automation Exercise](https://automationexercise.com)
* **Automation Script**: [`Project1/Python_Automation.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation.py)
* **Execution Report**: [`Project1/execution_report.md`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/execution_report.md)
* **Evidence Screenshot**: [`Project1/order_evidence.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/order_evidence.png)
* **Key Steps**: End-to-end user journey automation including user registration, catalog navigation, product search (`tshirt`), cart quantity modification, checkout flow, and automated evidence capture.

### 🌐 Website 2: TutorialsNinja Demo (`https://tutorialsninja.com/demo/`)
* **Target Website**: [TutorialsNinja Demo](https://tutorialsninja.com/demo/)
* **Automation Script**: [`Project1/Python_Automation2.py`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/Python_Automation2.py)
* **Execution Report**: [`Project1/execution_report2.md`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/execution_report2.md)
* **Evidence Screenshot**: [`Project1/cart_screenshot.png`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project1/cart_screenshot.png)
* **Demonstration Video**: [▶️ Watch TutorialsNinja Demonstration Video on Google Drive](https://drive.google.com/drive/folders/1klwyIyQB7_FPjgkBRubDaGUtmnzWuREI?usp=sharing)
* **Key Steps**: Customer lifecycle automation covering dynamic user registration, multi-category product selection (Mac, Tablets), adding products to cart, dynamic quantity modification, and cart state verification.

---

## 📌 Project 2: Selenium Python Framework Development (Unittest + PyTest + POM)

Enterprise Selenium Python Automation Framework automating Login and Product Search functionalities of [TutorialsNinja Demo](https://tutorialsninja.com/demo/).

* **Framework Directory**: [`Project2/`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/)
* **Framework Overview & Guide**: [`Project2/README.md`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/README.md)
* **Detailed Execution Report**: [`Project2/execution_report.md`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/execution_report.md)
* **Interactive HTML Report**: [`Project2/reports/pytest_report.html`](file:///d:/projects/selenium_assignment/Selenium/Folder%202%20-%20Capstone%20Project/Project2/reports/pytest_report.html)
* **Key Features**: Page Object Model (POM), Dual Unittest & PyTest test runners, CSV Data-Driven Testing (`login_data.csv`, `search_data.csv`), `config.ini` management, dynamic `DriverFactory`, timestamped failure/step screenshot capture.

---

## 🎥 Demonstration Video Links

* **TutorialsNinja Demo Video Demonstration**:  
  [▶️ Watch TutorialsNinja Demonstration Video on Google Drive](https://drive.google.com/drive/folders/1klwyIyQB7_FPjgkBRubDaGUtmnzWuREI?usp=sharing)

---

## 📂 Directory Structure

```text
Folder 2 - Capstone Project/
├── README.md
├── Project1/
│   ├── Python_Automation.py      # Script for Website 1 (Automation Exercise)
│   ├── Python_Automation2.py     # Script for Website 2 (TutorialsNinja Demo)
│   ├── execution_report.md       # Report for Website 1
│   ├── execution_report2.md      # Report for Website 2
│   ├── order_evidence.png        # Evidence screenshot for Website 1
│   └── cart_screenshot.png       # Evidence screenshot for Website 2
└── Project2/
    ├── config/                   # Configuration management (config.ini, config_reader.py)
    ├── test_data/                # CSV test datasets (login_data.csv, search_data.csv)
    ├── utilities/               # Utility classes (DriverFactory, CSVReader, ScreenshotUtility)
    ├── pages/                    # Page Object Model (BasePage, HomePage, LoginPage, AccountPage, SearchResultsPage)
    ├── tests/                    # Unittest + Pytest test cases (test_login.py, test_search.py)
    ├── reports/                  # Generated HTML reports (pytest_report.html)
    ├── screenshots/              # Evidence & failure screenshot captures
    ├── conftest.py               # Pytest configuration, fixtures & report hooks
    ├── pytest.ini                # Pytest settings
    ├── run_tests.py              # CLI test suite runner script
    ├── requirements.txt          # Python dependencies
    ├── README.md                 # Framework documentation
    └── execution_report.md       # Test execution report
```
