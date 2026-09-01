import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj = Service("D:/downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# Service("chromedriver.exe")

# driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.get("https://leetcode.com")

driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)