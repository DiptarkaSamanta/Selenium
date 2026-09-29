from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    MY_ACCOUNT_HEADING = (By.XPATH, "//h2[text()='My Account']")
    LOGOUT_RIGHT_LINK = (By.XPATH, "//aside//a[text()='Logout' or normalize-space()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_my_account_heading_displayed(self):
        return self.is_element_displayed(self.MY_ACCOUNT_HEADING, timeout=5)

    def is_logout_option_available(self):
        return self.is_element_displayed(self.LOGOUT_RIGHT_LINK, timeout=5)
