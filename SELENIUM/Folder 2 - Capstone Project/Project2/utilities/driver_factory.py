from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config.config_reader import ConfigReader

class DriverFactory:
    @staticmethod
    def get_driver(browser_name=None, headless=None):
        if browser_name is None:
            browser_name = ConfigReader.get_browser()
        if headless is None:
            headless = ConfigReader.is_headless()

        browser_name = browser_name.lower().strip()
        driver = None

        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_name}")

        implicit_wait = ConfigReader.get_implicit_wait()
        driver.implicitly_wait(implicit_wait)
        driver.maximize_window()
        return driver
