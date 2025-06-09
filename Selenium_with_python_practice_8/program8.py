from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")  #window-1

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Selenium Books")

driver.find_element(By.ID,"nav-search-submit-button").click()

driver.find_element(By.XPATH,"//span[contains(text(),'Selenium with Java – A Beginner’s Guide: Web Browser Automation')]").click() #window-2

driver.find_element(By.XPATH,"//span[contains(text(),'Selenium Grid for E-Commerce, Healthcare, EdTech, Banking, and SAAS')]").click() #window-3

print(driver.window_handles)

for id in driver.window_handles:
    driver.switch_to.window(id)
    if driver.title._contains_("Selenium with Java – A Beginner’s Guide: Web Browser Automation for Testing using Selenium with Java"):
        driver.find_element(By.ID,"add-to-cart-button").click()
        driver.close()
    elif driver.current_url._contains_("Ultimate-Selenium-WebDriver-Automation-Commerce"):
        driver.find_element(By.ID,"add-to-cart-button").click()
    else:
        driver.close()

time.sleep(5)
