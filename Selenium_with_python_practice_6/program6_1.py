import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("https://demo.guru99.com/test/drag_drop.html")

src = driver.find_element(By.XPATH,"//li[@data-id='2']")
trg = driver.find_element(By.XPATH,"//ol[@id='amt7']")
time.sleep(4)
ActionChains(driver).drag_and_drop(src,trg).perform()

src = driver.find_element(By.XPATH,"//li[@id='credit2']")
trg = driver.find_element(By.XPATH,"//ol[@id='bank']")

ActionChains(driver).drag_and_drop(src,trg).perform()
