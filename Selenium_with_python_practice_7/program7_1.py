import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

src = driver.find_element(By.XPATH,"//span[text()='right click me']")

ActionChains(driver).context_click(src).perform()

ActionChains(driver).click(driver.find_element(By.XPATH,"//span[text()='Cut']")).perform()

time.sleep(5)
