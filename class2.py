# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# import time
#
# browsername = "chrome"
#
# if browsername.lower() == "chrome":
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# elif browsername.lower() == "firefox":
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
# else:
#     raise Exception("Unsupported Browser")
#
# driver.get("https://testautomationpractice.blogspot.com")
# driver.maximize_window()
#
# time.sleep(2)
#
# driver.find_element(By.XPATH, "//input[@id='name']").send_keys("pythonjoker")
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
# driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("123456790")
# driver.find_element(By.XPATH, "//input[@id='address']").send_keys("kolkata, 700156")
# # driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("123456790")
#
# # gender_radio_button = driver.find_element(By.XPATH, "//input[@value='radio1']")
# # gender_radio_button.click()
# driver.find_element(By.XPATH, "//input[@id='male']").click()
#
# time.sleep(3)
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
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

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("pythonjoker")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("123456790")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("kolkata, 700156")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='male']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='tuesday']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='wednesday']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='thursday']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='friday']").click()
time.sleep(1)
Select(driver.find_element(By.XPATH, "//select[@id='country']")).select_by_value("india")
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='blue']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='fox']").click()
time.sleep(1)
date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date.click()
time.sleep(1)
# Select date 16
driver.find_element(By.XPATH, "//a[@data-date='16']").click()
time.sleep(1)


# time.sleep(1)
#
# date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
# date.click()
#
# target_date = "16-September-2027"

# Split the target date
# day, month, year = target_date.split("-")
#
# # Keep changing the calendar until the correct month and year appear
# while True:
#     current_month = driver.find_element(
#         By.XPATH, "//span[@class='ui-datepicker-month']"
#     ).text
#
#     current_year = driver.find_element(
#         By.XPATH, "//span[@class='ui-datepicker-year']"
#     ).text
#
#     # Stop when target month and year are reached
#     if current_month == month and current_year == year:
#         break
#
#     # Move to next month
#     driver.find_element(By.XPATH, "//a[@title='Next']").click()
#
# # Select the required day
# driver.find_element(
#     By.XPATH, f"//a[@data-date='{day}']"
# ).click()

target_day = "16"
target_month = "Sep"
target_year = "2026"

date = driver.find_element(By.XPATH, "//input[@id='txtDate']")
date.click()

time.sleep(1)
# Select month
month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
month.select_by_visible_text(target_month)

# Select year
year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
year.select_by_visible_text(target_year)

# Select day
driver.find_element(
    By.XPATH,
    f"//a[@data-date='{target_day}']"
).click()


time.sleep(3)

driver.quit()