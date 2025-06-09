from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def application(driver,url):
    driver.get(url)

def type(driver,xpath,data):
    driver.find_element(By.XPATH, xpath).send_keys(data)

def clickIn(driver,xpath):
    driver.find_element(By.XPATH, xpath).click()

def clearAll(driver,xpath):
    driver.find_element(By.XPATH, xpath).clear()

def verifyTitle(driver,actualTitle):
    assert driver.title._eq_(actualTitle), "User landed in wrong application"

def verifyCurrentUrl(driver,actualTitle):
    assert driver.current_url._eq_(actualTitle), "User landed in wrong application"

def getTextAndVerify(driver,xpath,actualText):
    txtValue= driver.find_element(By.XPATH, xpath).text
    assert txtValue._eq_(actualText)

def verifyElementIsDisplay(driver,xpath):
    assert driver.find_element(By.XPATH, xpath).is_displayed, "Element is not displayed"
