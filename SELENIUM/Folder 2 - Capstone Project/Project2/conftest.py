import pytest
import os
import time
from utilities.driver_factory import DriverFactory
from utilities.screenshot_utility import ScreenshotUtility
from config.config_reader import ConfigReader

@pytest.fixture(scope="function")
def setup_driver(request):
    driver = DriverFactory.get_driver()
    base_url = ConfigReader.get_base_url()
    driver.get(base_url)
    
    # Pass driver instance to test class if using unittest
    if request.cls:
        request.cls.driver = driver
        
    yield driver
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture screenshots on test failure and embed into HTML report."""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = None
        if "setup_driver" in item.fixturenames:
            driver = item.funcargs.get("setup_driver")
        elif item.instance and hasattr(item.instance, "driver"):
            driver = item.instance.driver

        if driver:
            screenshot_path = ScreenshotUtility.capture_screenshot(
                driver, f"FAILURE_{item.name}"
            )
            if screenshot_path and os.path.exists(screenshot_path):
                # Import pytest_html extra if present
                try:
                    import pytest_html
                    rel_path = os.path.relpath(screenshot_path, start="reports")
                    html = f'<div><img src="{rel_path}" alt="screenshot" style="width:600px;height:auto;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extras.append(pytest_html.extras.html(html))
                except Exception as e:
                    print(f"[conftest] Could not attach screenshot to html report: {e}")
    report.extras = extras

def pytest_html_report_title(report):
    report.title = "Selenium Automation Framework Execution Report - Project 2"
