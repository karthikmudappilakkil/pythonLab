
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open browser
driver = webdriver.Chrome()

try:
    # Open website
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    print("Enter the details in the browser, then click Submit.")
    input("Press Enter in this terminal after clicking Submit...")

    # Fetch output only after the user submits the form
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#output #name"))
    )

    print("\nSubmitted Details:")
    print(driver.find_element(By.CSS_SELECTOR, "#output #name").text)
    print(driver.find_element(By.CSS_SELECTOR, "#output #email").text)
    print(driver.find_element(By.CSS_SELECTOR, "#output #currentAddress").text)
    print(driver.find_element(By.CSS_SELECTOR, "#output #permanentAddress").text)

    input("\nPress Enter to close browser")
finally:
    # Close browser
    driver.quit()