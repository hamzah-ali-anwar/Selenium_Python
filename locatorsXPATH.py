# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)  # Keeps browser open
service = Service("/usr/bin/chromedriver")  # Ensure correct path

# Create a driver object from Chrome class
driver = webdriver.Chrome(service=service, options=options)

# Implicit wait
driver.implicitly_wait(5)

# Test begins
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']").click()

actual_title = driver.find_element(By.XPATH, "//div[@class='app_logo']").text
expected_title = "Swag Labs"

if actual_title == expected_title:
    print("Title is correct")
else:
    print("Incorrect title")

driver.close()