# Selenium Automation Demo: Registration Form

This Python script demonstrates how to automate filling out a registration form using Selenium WebDriver with Firefox. The script navigates to the demo registration page, enters sample data into form fields, interacts with radio buttons and checkboxes, and showcases the use of various Selenium commands.

## Features

- Opens the demo registration page: [https://demo.automationtesting.in/Register.html](https://demo.automationtesting.in/Register.html)
- Fills out the following form fields:
  - First Name
  - Last Name
  - Address
  - Email
- Selects a gender radio button
- Selects and deselects a hobbies checkbox
- Demonstrates clearing input fields

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

1. Save the following code as `register_form_automation.py`:

2. **Run the script:**
   ```bash
   python register_form_automation.py
   ```

## Notes

- Ensure `geckodriver` is available in your PATH so Selenium can launch Firefox.
- The script demonstrates basic automation. You can extend it to fill out the rest of the form or add assertions for automated testing.
- The script opens the browser and performs actions visibly. For headless mode, update the WebDriver initialization accordingly.

## References

- [Selenium with Python Documentation](https://selenium-python.readthedocs.io/)
- [Automation Testing Demo Site](https://demo.automationtesting.in/Register.html)
- [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases)
