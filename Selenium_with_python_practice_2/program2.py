from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://demo.automationtesting.in/Register.html")

# used to find the web elements and sends the desired input
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("TEST A")

driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("TEST B")

driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Chennai -06")

driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys("test01@gmail.com")

#clicks the desired clicable button
driver.find_element(By.XPATH,"//input[@value='Male']").click()

driver.find_element(By.XPATH,"//input[@value='Cricket']").click()

# clears the previously entered data
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").clear()

driver.find_element(By.XPATH,"//input[@value='Cricket']").click()

driver.close()
