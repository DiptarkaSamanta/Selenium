from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

try:
    print("=================================================================")
    print("DEMO: HANDLING DYNAMIC ELEMENTS & TRAVERSING WEBTABLES")
    print("=================================================================")

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    time.sleep(2)

    # 1. Locate WebTable and count Rows & Columns
    table = driver.find_element(By.XPATH, "//table[@name='courses']")
    rows = driver.find_elements(By.XPATH, "//table[@name='courses']//tr")
    total_rows = len(rows)
    
    cols = driver.find_elements(By.XPATH, "//table[@name='courses']//tr[1]/th")
    total_cols = len(cols)

    print(f"Total Rows: {total_rows}")
    print(f"Total Columns: {total_cols}")

    # 2. Extract and print Header Columns
    headers = [col.text for col in cols]
    print(f"Table Headers: {headers}")

    print("\n--- Traversing Entire WebTable ---")
    # 3. Traverse through table rows & columns
    for r in range(2, total_rows + 1):
        row_values = []
        for c in range(1, total_cols + 1):
            cell_data = driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[{c}]").text
            row_values.append(cell_data)
        print(f"Row {r - 1}: {row_values}")

    print("\n--- Conditional Search in WebTable ---")
    # 4. Search for courses priced at 25 and print course title
    for r in range(2, total_rows + 1):
        price_text = driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[3]").text
        if price_text == "25":
            course_title = driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[2]").text
            print(f"Found Course priced $25: '{course_title}'")

    print("\n--- Summing Numeric Column Values ---")
    # 5. Sum all course prices
    total_sum = 0
    for r in range(2, total_rows + 1):
        price_text = driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[3]").text
        total_sum += int(price_text)
    
    print(f"Total Sum of all Course Prices: ${total_sum}")

finally:
    time.sleep(2)
    driver.quit()
    print("\nBrowser Session Closed Successfully.")
