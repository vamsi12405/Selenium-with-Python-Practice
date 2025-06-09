# Amazon Multi-Tab Product Adder (Selenium Python)

This Python script leverages Selenium WebDriver to automate Browse on Amazon, specifically demonstrating how to handle multiple browser tabs (or windows) and add products to the shopping cart.

## About the Project

This project serves as an example of advanced web automation using Selenium in Python. It simulates a user scenario where multiple product pages are opened in separate tabs from a search results page or a list of URLs, and then products from each of these tabs are added to the Amazon shopping cart. This is particularly useful for learning how to switch between browser windows/tabs (`window_handles`) and manage context in automated scripts.

## Features

* Opens multiple Amazon product pages in new tabs.
* Successfully switches between tabs using Selenium's `window_handles`.
* Adds products to the cart from different tabs.
* Designed for demonstration and educational purposes regarding Selenium window handling.
* (Optional: Add more specific features if your script has them, e.g., "Reads product URLs from a file," "Handles CAPTCHAs/login if implemented," etc.)

## Getting Started

To get a local copy of this project up and running, follow these simple steps.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
* **pip**: Python's package installer (usually comes with Python).
* **Web Browser**: Chrome is commonly used, but you can adapt the script for Firefox, Edge, etc.
* **WebDriver**: The correct WebDriver for your chosen browser.
    * **ChromeDriver
