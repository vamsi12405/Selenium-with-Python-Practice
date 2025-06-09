import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH,"//input[@value='Cricket']").click()

assert driver.find_element(By.XPATH,"//input[@value='Cricket']").is_selected(),"Cricket Field is not selected in web page"

time.sleep(4)
