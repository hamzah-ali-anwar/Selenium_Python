# Test Case
# 1) Open Web Browser (Chrome/Firefix)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username: Admin
# 4) Enter password: admin123
# 5) Click on login
# 6) Capture title of the home page.
# 7) Verify title of the page: OrangeHRM
# 8) Close browser

# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
service = Service("/usr/bin/chromedriver")  # Correct path

# Create a driver object from chrome class
driver = webdriver.Chrome(service=service, options=options)

# Set Implicit Wait (applies globally to all elements)
driver.implicitly_wait(10)

# Test Case Verification Begins
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Test passed")
else:
    print("Test Failed")

driver.close()


