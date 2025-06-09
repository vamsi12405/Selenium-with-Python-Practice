import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

assert driver.find_element(By.ID,"user-name").is_enabled(),"Username Text Field is disabled in web page"

driver.find_element(By.ID,"user-name").send_keys("test@gmail.com")
time.sleep(4)
