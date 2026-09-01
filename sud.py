from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# ---------------- CSS SELECTOR ----------------
# Find Form Authentication link
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
print("Link:", link.text)

# Click Form Authentication
link.click()
time.sleep(2)


# ---------------- CSS WILDCARD SELECTOR ----------------
# ID starts with "user"
username = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
username.send_keys("tomsmith")
time.sleep(1)


# ---------------- CSS WILDCARD SELECTOR ----------------
# ID ends with "word"
password = driver.find_element(By.CSS_SELECTOR, "input[id$='word']")
password.send_keys("SuperSecretPassword!")
time.sleep(1)


# ---------------- CSS SELECTOR ----------------
# Find login button
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
print("Button:", login_button.text)

login_button.click()
time.sleep(2)

driver.quit()