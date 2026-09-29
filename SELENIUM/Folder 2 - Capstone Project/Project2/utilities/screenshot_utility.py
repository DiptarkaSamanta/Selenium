import os
import time

class ScreenshotUtility:
    @staticmethod
    def capture_screenshot(driver, name_prefix="screenshot"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir = os.path.join(base_dir, "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{name_prefix}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)

        try:
            driver.save_screenshot(filepath)
            print(f"[ScreenshotUtility] Saved screenshot to: {filepath}")
            return filepath
        except Exception as e:
            print(f"[ScreenshotUtility] Failed to capture screenshot: {e}")
            return None
