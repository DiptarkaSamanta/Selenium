from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:
    driver.get("https://google.com")
    time.sleep(5)
    print("page title:", driver.title)
    language_link = driver.find_elements(By.LINK_TEXT, "English")
    language_link.click()
    time.sleep(5)
finally:
    driver.quit()