# Selenium Element State Checker (Python)

A Python project utilizing Selenium WebDriver to demonstrate and assert the state of web elements using `is_displayed()`, `is_enabled()`, and `is_selected()`.

## About the Project

This project provides a practical example of how to use Selenium's built-in methods to check the current state of various web elements. These checks are fundamental for building reliable and resilient automation scripts, ensuring that your script interacts with elements only when they are in the expected state (e.g., visible, clickable, or selected).

The script will typically:
* Navigate to a web page containing different types of elements (e.g., text fields, buttons, checkboxes, radio buttons).
* Use `is_displayed()` to verify if an element is visible on the page.
* Use `is_enabled()` to check if an interactive element (like a button or input field) is active and ready for interaction.
* Use `is_selected()` to determine if a checkbox or radio button is currently chosen.
* Print the results of these assertions to the console.

---

## Key Concepts

* **`element.is_displayed()`**: Returns `True` if the element is visible on the page, `False` otherwise. This checks for visibility, not just presence in the DOM. An element can exist in the HTML but be hidden by CSS (e.g., `display: none;`).
* **`element.is_enabled()`**: Returns `True` if the element is enabled (i.e., not disabled), `False` otherwise. This is commonly used for input fields and buttons to ensure they can be interacted with.
* **`element.is_selected()`**: Returns `True` if the element (typically a checkbox, radio button, or an `<option>` in a `<select>`) is currently selected, `False` otherwise.

---

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

You'll need Python, `pip` (Python's package installer), a web browser, and its corresponding WebDriver executable.

* **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
* **Web Browser**: Chrome is a popular choice, but Firefox, Edge, etc., work too.
* **WebDriver**: Download the appropriate WebDriver for your chosen browser and ensure it's accessible from your system's PATH, or specify its path in the script.
    * **ChromeDriver**: For Google Chrome, get it from [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). Make sure the version matches your Chrome browser.
    * **GeckoDriver**: For Mozilla Firefox, find it at [github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases).=

### How to Run

1.  **Configure WebDriver Path (if needed):**
    Open your Python script (e.g., `element_state_checker.py`). If your WebDriver isn't in your system's PATH, you'll need to specify its location.

    Example for Chrome:
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    # Update this path if ChromeDriver is not in your PATH
    service = Service('/path/to/your/chromedriver')
    driver = webdriver.Chrome(service=service)
    ```

2.  **Execute the script:**
    Navigate to the project directory in your terminal or command prompt and run:

    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `element_state_checker.py`.)

The script will launch a browser, navigate to a target page, perform the checks, and print the results to your console.

---

## How It Works

The core of the script involves:

1.  **Initializing WebDriver**: Setting up the browser instance.
2.  **Navigating**: Opening a specific URL (ideally, a page with elements to test).
3.  **Locating Elements**: Using methods like `find_element_by_id()`, `find_element_by_name()`, `find_element_by_xpath()`, etc., to get a reference to the desired web elements.
4.  **Applying Assertions**: Calling `.is_displayed()`, `.is_enabled()`, and `.is_selected()` on the located elements.
5.  **Reporting**: Printing the boolean result of each check.
6.  **Quitting Driver**: Closing the browser session gracefully.


## Contact

Your Name - your_email@example.com

Project Link: [https://github.com/YOUR_USERNAME/selenium-element-state-checker](https://github.com/YOUR_USERNAME/selenium-element-state-checker)
