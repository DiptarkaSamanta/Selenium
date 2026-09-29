from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account' or normalize-space()='My Account']")
    MY_ACCOUNT_ICON = (By.XPATH, "//i[contains(@class, 'fa-user')]")
    LOGIN_LINK = (By.XPATH, "//a[text()='Login' or normalize-space()='Login']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Register' or normalize-space()='Register']")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//div[@id='search']//button")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self, url):
        self.driver.get(url)

    def open_my_account_menu(self):
        try:
            self.click(self.MY_ACCOUNT_DROPDOWN)
        except Exception:
            self.click(self.MY_ACCOUNT_ICON)

    def click_login(self):
        self.open_my_account_menu()
        self.click(self.LOGIN_LINK)

    def click_register(self):
        self.open_my_account_menu()
        self.click(self.REGISTER_LINK)

    def search_for_product(self, keyword):
        self.send_keys(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
