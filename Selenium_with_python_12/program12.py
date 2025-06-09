from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(25)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("TEST")

wait = WebDriverWait(driver,20,poll_frequency=10)
wait.until(exp.presence_of_element_located((By.ID,"password")))
wait.until(exp.alert_is_present())
wait.until(exp.title_is())
wait.until(exp.new_window_is_opened())
wait.until(exp.frame_to_be_available_and_switch_to_it(("")))

driver.find_element(By.ID,"passwords").send_keys("TEST")
