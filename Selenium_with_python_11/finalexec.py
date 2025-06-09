import time

from selenium import webdriver
from SeleniumProject import HomePage as hp
from SeleniumProject import Framework as fw
from SeleniumProject import ProductsPage as pp

driver = webdriver.Chrome()

def testCase01():
    fw.application(driver,"https://www.saucedemo.com/")
    hp.verifyHomePage(driver)
    hp.verifyUserDeatils(driver)
    hp.logIn(driver)

def testCase02():
    pp.verifyProductsPage(driver)
    pp.addToCart(driver)
    time.sleep(10)
