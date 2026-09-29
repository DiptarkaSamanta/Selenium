from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_HEADER = (By.XPATH, "//h1[contains(text(), 'Search')]")
    PRODUCT_TITLES = (By.XPATH, "//div[contains(@class, 'product-thumb')]//h4/a")
    NO_PRODUCT_MSG = (By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria')]")
    PRODUCT_CONTAINER = (By.XPATH, "//div[contains(@class, 'product-layout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_search_header_displayed(self):
        return self.is_element_displayed(self.SEARCH_HEADER)

    def get_product_titles(self):
        try:
            self.wait.until(lambda d: len(d.find_elements(*self.PRODUCT_TITLES)) > 0 or len(d.find_elements(*self.NO_PRODUCT_MSG)) > 0)
        except Exception:
            pass

        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text.strip() for el in elements if el.text.strip()]

    def is_product_displayed(self, product_name):
        titles = self.get_product_titles()
        return any(product_name.lower() in title.lower() for title in titles)

    def get_no_product_message(self):
        if self.is_element_displayed(self.NO_PRODUCT_MSG, timeout=5):
            return self.get_text(self.NO_PRODUCT_MSG)
        return ""

    def get_product_count(self):
        return len(self.get_product_titles())
