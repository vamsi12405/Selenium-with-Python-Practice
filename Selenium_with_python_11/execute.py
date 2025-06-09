from SeleniumProject import Framework as fw

def verifyHomePage(driver):
    fw.verifyTitle(driver,"Swag Labs")
    fw.verifyCurrentUrl(driver,"https://www.saucedemo.com/")
    fw.getTextAndVerify(driver,"//div[@class='login_logo']","Swag Labs")

def verifyUserDeatils(driver):
    fw.verifyElementIsDisplay(driver,"//input[@data-test='username']")
    fw.verifyElementIsDisplay(driver, "//input[@data-test='password']")
    fw.verifyElementIsDisplay(driver, "//input[@data-test='login-button']")

def logIn(driver):
    fw.type(driver,"//input[@data-test='username']","standard_user")
    fw.type(driver, "//input[@data-test='password']", "secret_sauce")
    fw.clickIn(driver,"//input[@data-test='login-button']")
