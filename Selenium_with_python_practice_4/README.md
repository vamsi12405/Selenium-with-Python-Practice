# Selenium Alerts Handling Example

This Python script demonstrates how to automate the handling of different types of JavaScript alerts using Selenium WebDriver with Firefox. It covers simple alerts, confirm dialogs, and prompt dialogs on the [Automation Testing Alerts Demo](https://demo.automationtesting.in/Alerts.html) page.

## Features

- Opens the demo alerts page.
- Handles:
  - **Simple Alerts:** Reads and accepts alert messages.
  - **Confirm Alerts:** Reads messages and demonstrates both accepting and dismissing.
  - **Prompt Alerts:** Reads the message, sends input text, and accepts the prompt.
- Includes delays (`time.sleep`) for demonstration purposes.

## Prerequisites

- Python 3.x
- [Selenium](https://selenium-python.readthedocs.io/)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)

## Installation

1. **Install Selenium:**
   ```bash
   pip install selenium
   ```

2. **Download GeckoDriver:**
   - Download for your OS from [here](https://github.com/mozilla/geckodriver/releases).
   - Add the downloaded executable to your system PATH.

## Usage

1. Save the following code as `alerts_handling.py`:

   ```python
   import time
   from selenium import webdriver
   from selenium.webdriver.common.by import By

   driver = webdriver.Firefox()

   driver.get("https://demo.automationtesting.in/Alerts.html")

   # Simple alert
   driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
   time.sleep(2)
   print(driver.switch_to.alert.text)
   driver.switch_to.alert.accept()

   # Confirm alert
   driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
   driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
   time

