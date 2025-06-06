# Selenium Automation Demo: Dropdowns and Multiselect Example

This Python script demonstrates how to automate dropdown and multiselect element interactions using Selenium WebDriver with Firefox. It navigates to the [Automation Testing Registration Demo](https://demo.automationtesting.in/Register.html), selects values from dropdowns, and interacts with a multi-select language field.

## Features

- Opens the Automation Testing registration page.
- Demonstrates how to select options from a dropdown using:
  - `select_by_index` (commented in example)
  - `select_by_value` (commented in example)
  - `select_by_visible_text` (active in example)
- Demonstrates multi-select interaction for languages.

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


1. **Run the script:**
   ```bash
   python dropdown_multiselect_automation.py
   ```

## Notes

- Ensure `geckodriver` is available in your PATH so Selenium can launch Firefox.
- The usage of `Select` demonstrates different ways to select options from a dropdown by index, value, or visible text.
- The language multiselect is demonstrated by clicking to open and then selecting multiple languages.
- You can uncomment and use the other select examples as needed.

## References

- [Selenium with Python Documentation](https://selenium-python.readthedocs.io/)
- [Automation Testing Demo Site](https://demo.automationtesting.in/Register.html)
- [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases)
