# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
service = Service("/usr/bin/chromedriver")  # Ensure correct path

# Create a driver object from Chrome class
driver = webdriver.Chrome(service=service, options=options)

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field and enter credentials
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")

# Wait for the login button and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))).click()

# Verify title
actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test passed")
else:
    print("Test Failed")

driver.close() 