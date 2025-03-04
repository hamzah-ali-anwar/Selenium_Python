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

# CSS selectors
# 1. tag Id
# 2. tag class 
# 3. tag attribute
# 4. tag class attribute

# 1. tag Id
# driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")

# 2. tag class 
# driver.find_element(By.CSS_SELECTOR, "input.input_error.form_input").send_keys("standard_user")

# 3. tag attribute
# driver.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys("standard_user")

# 4. tag class attribute
driver.find_element(By.CSS_SELECTOR, "input.input_error.form_input[placeholder=Username]").send_keys("standard_user")
