from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(
    r"D:\downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)

driver = webdriver.Chrome(service=service)

driver.get("https://example.com")

print(driver.title)

driver.quit()