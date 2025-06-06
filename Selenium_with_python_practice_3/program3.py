from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

# gets the website
driver.get("https://demo.automationtesting.in/Register.html")

# usage of select slatement by index in option tag
#Select(driver.find_element(By.XPATH,"//select[@ng-model='Skill']")).select_by_index(8)

# usage of select by value in options tag
#Select(driver.find_element(By.XPATH,"//select[@ng-model='Skill']")).select_by_value("Adobe Photoshop")

# usage of select statement by text in option tag
Select(driver.find_element(By.XPATH,"//select[@ng-model='Skill']")).select_by_visible_text("Desktop Publishing")

driver.find_element(By.ID,"msdd").click()

driver.find_element(By.XPATH,"//a[text()='Arabic']").click()

driver.find_element(By.XPATH,"//a[text()='Dutch']").click()

driver.close()
