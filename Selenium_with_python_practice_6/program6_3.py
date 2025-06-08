import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")

src = driver.find_element(By.ID,"submitbtn")

ActionChains(driver).scroll_to_element(src).perform()

time.sleep(5)
