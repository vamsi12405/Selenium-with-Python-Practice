import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

assert driver.find_element(By.ID,"user-name").is_displayed(),"Username Text Field is not displayed in web page"
assert driver.find_element(By.ID,"password").is_displayed(),"Password Text Field is not displayed in web page"
assert driver.find_element(By.ID,"login-button").is_displayed(),"Log-in Button Field is not displayed in web page"

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(4)
