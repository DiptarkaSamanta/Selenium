from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

else:
    raise Exception("Unsupported Browser")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

time.sleep(2)
radio_button = driver.find_element(By.XPATH, "//input[@value='radio1']")
# Click it
radio_button.click()

dropdown = driver.find_element(By.ID, "dropdown-class-example")
dropdown.click()

time.sleep(2)

driver.find_element(By.XPATH, "//option[@value='option1']").click()

time.sleep(3)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# for checkbox in checkboxes:
#     if not checkbox.is_selected():
#         checkbox.click()

checkbox1 = driver.find_element(By.ID, "checkBoxOption1")
checkbox1.click()

# time.sleep(2)

checkbox2 = driver.find_element(By.ID, "checkBoxOption2")
checkbox2.click()

# time.sleep(2)

checkbox3 = driver.find_element(By.ID, "checkBoxOption3")
checkbox3.click()

driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Germany")

time.sleep(2)

driver.find_element(By.XPATH, "//li[text()='Germany']").click()

time.sleep(3)

# time.sleep(3)
# driver.find_element(By.ID, "autocomplete").send_keys("Germany")
# options = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
# for option in options:
#     if option.text == "Germany":
#         option.click()
#         break
time.sleep(3)

driver.quit()