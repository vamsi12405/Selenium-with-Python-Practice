import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.get("https://demo.guru99.com/test/drag_drop.html")

ActionChains(driver).scroll_by_amount(0,400).perform()

src = driver.find_element(By.XPATH,"//li[@id='credit2']")
trg = driver.find_element(By.XPATH,"//ol[@id='bank']")

ActionChains(driver).drag_and_drop(src,trg).perform()
