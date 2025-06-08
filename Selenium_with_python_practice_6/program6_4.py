import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.myntra.com/")

src = driver.find_element(By.XPATH,"//div[@class='desktop-navLinks']//child::div//a[text()='Genz']")

ActionChains(driver).move_to_element(src).perform()

time.sleep(5)
