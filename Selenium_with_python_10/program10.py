from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/web-table-element.php")

expectedHeaderList = ["Company","Group","Prev Close (Rs)","Current Price (Rs)","% Change"]

listOfCompanyElements = driver.find_elements(By.XPATH,"//table[@class='dataTable']//tbody//tr//td")

count=0
for companyElement in listOfCompanyElements:
    print(companyElement.text,end=",")
    count+=1
    if count==5:
        print("")
        count=0
