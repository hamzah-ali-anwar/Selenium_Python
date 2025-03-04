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

# Implicit wait
driver.implicitly_wait(5)

# Test begins
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Id and xpath locators
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo IdeaCentre")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

#linktext & partial linktext
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

# Class name & tag name
product_item = driver.find_elements(By.CLASS_NAME, "product-item")
print(len(product_item))

# CSS selectors