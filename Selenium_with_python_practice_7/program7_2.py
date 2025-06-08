import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")

src = driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")

ActionChains(driver).double_click(src).perform()


time.sleep(5)
