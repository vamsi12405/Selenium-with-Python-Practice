import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demo.automationtesting.in/Frames.html")

# used to switch to single frame
driver.switch_to.frame("singleframe")

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("TESTA")

driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[@href='#Multiple']").click()


driver.switch_to.frame("singleframe")

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("TESTA")

time.sleep(5)

driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[@href='#Multiple']").click()


driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']"))

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("TESTB")
