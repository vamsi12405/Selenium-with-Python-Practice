import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demo.automationtesting.in/Frames.html")

# used to switch to single frame
driver.switch_to.frame("singleframe")

# used to find element in the iframe and send the defired input
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("TESTA")

# comes out of iframe window
driver.switch_to.default_content()

time.sleep(5)

# used to click the multiframe button
driver.find_element(By.XPATH,"//a[@href='#Multiple']").click()

# moves into first multiframe(outer frame) and then inner frame(single frame)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']"))

# sends the desired input
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("TESTB")
