import unittest
import pytest
from utilities.driver_factory import DriverFactory
from utilities.csv_reader import CSVReader
from utilities.screenshot_utility import ScreenshotUtility
from config.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = ConfigReader.get_base_url()

    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.driver.get(self.base_url)
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)

    def tearDown(self):
        try:
            if hasattr(self, "driver") and self.driver:
                self.driver.quit()
        except Exception:
            pass

    @pytest.mark.search
    def test_search_existing_products_csv(self):
        """Test search functionality for valid products loaded from CSV file."""
        search_data = CSVReader.read_csv_data("test_data/search_data.csv")
        found_rows = [row for row in search_data if row.get("expected_outcome") == "found"]

        for data in found_rows:
            keyword = data.get("search_keyword")
            expected_name = data.get("expected_product_or_msg")

            print(f"[TEST] Searching for valid product keyword: '{keyword}'")
            self.home_page.search_for_product(keyword)

            # Verify search page header
            self.assertTrue(self.search_results_page.is_search_header_displayed(), "Search results header was not displayed.")

            # Verify product appears in results
            product_displayed = self.search_results_page.is_product_displayed(expected_name)
            print(f"[TEST] Results for '{keyword}': Titles = {self.search_results_page.get_product_titles()}")

            self.assertTrue(
                product_displayed,
                f"Expected product '{expected_name}' was not found in search results for keyword '{keyword}'."
            )
            # Capture screenshot
            ScreenshotUtility.capture_screenshot(self.driver, f"EVIDENCE_search_{keyword.replace(' ', '_')}")

            # Navigate back to home for next iteration
            self.driver.get(self.base_url)

    @pytest.mark.search
    def test_search_non_existing_product_csv(self):
        """Test search functionality for non-existing products loaded from CSV file."""
        search_data = CSVReader.read_csv_data("test_data/search_data.csv")
        not_found_rows = [row for row in search_data if row.get("expected_outcome") == "not_found"]

        for data in not_found_rows:
            keyword = data.get("search_keyword")
            expected_msg = data.get("expected_product_or_msg")

            print(f"[TEST] Searching for non-existing product keyword: '{keyword}'")
            self.home_page.search_for_product(keyword)

            # Verify no product message
            actual_msg = self.search_results_page.get_no_product_message()
            print(f"[TEST] Received message: '{actual_msg}'")

            self.assertEqual(
                actual_msg,
                expected_msg,
                f"Expected message '{expected_msg}', but got '{actual_msg}' for search keyword '{keyword}'."
            )
            # Capture screenshot
            ScreenshotUtility.capture_screenshot(self.driver, f"EVIDENCE_search_non_existing_{keyword}")

    @pytest.mark.search
    def test_search_header_and_title(self):
        """Test searching keyword 'Mac' and validating result titles."""
        self.home_page.search_for_product("Mac")
        title = self.search_results_page.get_title()
        print(f"[TEST] Search Page Title: {title}")
        self.assertIn("Search - Mac", title, "Search page title does not contain search query.")
        ScreenshotUtility.capture_screenshot(self.driver, "EVIDENCE_search_header_and_title")

if __name__ == "__main__":
    unittest.main()
