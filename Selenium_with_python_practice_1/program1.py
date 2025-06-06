from selenium import webdriver

driver = webdriver.Firefox()

# this is used to connect to the website
driver.get("https://www.flipkart.com/")

# this pritns the title
print(driver.title)

# this fetches the current url
print(driver.current_url)

# this is used to close the driver connection to the browser
driver.close()

# this is used to terminate the session between driver and browser
#driver.quit()

# this is used to go back to the previous webpage
driver.back()

# this is used to go back to next webpage
driver.forward()

# this is used to refresh the webpage
driver.refresh()

# this is used to maximize the window
driver.maximize_window()

# this is used to minimize the window
driver.minimize_window()

# this makes the browser in full screen. Not to be used with back,forward,refresh commands.
driver.fullscreen_window()

# this is used to close the driver connection to the browser
driver.close()

# this is used to terminate the session between driver and browser
#driver.quit()
