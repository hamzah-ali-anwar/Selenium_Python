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

# Test begins here
driver.get("https://opensource-demo.orangehrmlive.com")

print(driver.title)