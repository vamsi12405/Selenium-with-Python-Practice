from SeleniumProject import Framework as fw


def verifyProductsPage(driver):
    fw.verifyTitle(driver,"Swag Labs")
    fw.verifyCurrentUrl(driver,"https://www.saucedemo.com/inventory.html")
    fw.getTextAndVerify(driver,"//div[@class='app_logo']","Swag Labs")


def addToCart(driver):
    fw.clickIn(driver,"//button[@data-test='add-to-cart-sauce-labs-backpack']")
    fw.clickIn(driver, "//button[@data-test='add-to-cart-sauce-labs-bike-light']")
    fw.clickIn(driver, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
