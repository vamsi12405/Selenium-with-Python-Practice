import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.accept()

driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.accept() 

driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.accept() 


driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.dismiss()
'''

driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()

time.sleep(5)

print(driver.switch_to.alert.text)

driver.switch_to.alert.send_keys("TESTER")

driver.switch_to.alert.accept()
