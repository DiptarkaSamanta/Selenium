import unittest
import pytest
from utilities.driver_factory import DriverFactory
from utilities.csv_reader import CSVReader
from utilities.screenshot_utility import ScreenshotUtility
from config.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = ConfigReader.get_base_url()

    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.base_url)
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)

    def tearDown(self):
        try:
            if hasattr(self, "driver") and self.driver:
                self.driver.quit()
        except Exception:
            pass

    @pytest.mark.login
    def test_invalid_login_scenarios_csv(self):
        """Test login with invalid credentials loaded from CSV data file."""
        login_data = CSVReader.read_csv_data("test_data/login_data.csv")
        invalid_rows = [row for row in login_data if row.get("expected_result") == "failure"]

        for index, data in enumerate(invalid_rows):
            # Ensure fresh login page navigation for each iteration
            self.driver.get(self.base_url)
            self.home_page.click_login()

            email = data.get("email", "")
            password = data.get("password", "")
            scenario = data.get("scenario", f"scenario_{index}")

            print(f"[TEST] Running invalid login scenario: '{scenario}' with Email: '{email}'")
            self.login_page.login(email, password)

            warning_msg = self.login_page.get_warning_message()
            print(f"[TEST] Received alert message: '{warning_msg}'")

            # Assert warning alert is present on login failure
            self.assertTrue(
                "Warning: No match for E-Mail Address and/or Password." in warning_msg or "Warning:" in warning_msg,
                f"Expected warning alert for scenario '{scenario}', but got: '{warning_msg}'"
            )
            # Capture evidence screenshot
            ScreenshotUtility.capture_screenshot(self.driver, f"EVIDENCE_invalid_login_{scenario}")

    @pytest.mark.login
    def test_login_page_navigation(self):
        """Test navigating from Home Page to Login Page and verifying page title."""
        self.home_page.click_login()
        title = self.login_page.get_title()
        print(f"[TEST] Login Page Title: {title}")
        self.assertEqual("Account Login", title, "Login page title does not match expected value.")
        ScreenshotUtility.capture_screenshot(self.driver, "EVIDENCE_login_page_navigation")

if __name__ == "__main__":
    unittest.main()
