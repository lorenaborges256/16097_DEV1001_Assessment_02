# Notify Me CLI Application

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-prototype-orange.svg)]()
[![Platform](https://img.shields.io/badge/platform-CLI-lightgrey.svg)]()
![Made with Cowsay](https://img.shields.io/badge/made%20with-cowsay-ff69b4?style=flat-square&logo=gnu&logoColor=white)

## Overview

The **Notify Me CLI Application** simulates a "Notify Me" feature commonly used in online stores. Users can register, browse available products, and request email notifications when out-of-stock items become available again.

This CLI tool is built for rapid testing and demonstrates the potential architecture and logic behind future live-inventory integrations with web platforms. Built as a prototype for future integration with e-commerce platforms.

## Features
- **User Account System**
  - Register with name and email (validated using RegEx)
  - Existing account lookup via `users.json`

- **Stock Interaction**
  - Add or delete products from `stock.txt`
  - View the current product list at any time

- **Email Notification**
  - Opt-in to receive email alerts when products are restocked
  - Emails sent using Gmail SMTP; credentials stored in `credentials.txt` (ignored by version control)

- **Session Monitoring**
  - Background stock monitor activates upon app exit
  - Ends when timeout occurs or product is back in stock
  - Logs refreshed per session via `sent_notifications.json`


## Developer Notes

- **Modules and its Purpose:** 
    - Standard Python library modules: 
        - `re`: Provides support for regular expressions, enabling pattern matching and text parsing. Useful for validating input formats or extracting structured data from strings.
        - `json`: Enables serialization and deserialization of data to and from JSON format. Ideal for reading/writing configuration files.
        - `os`: Offers a way to interact with the operating system, such as file paths, environment variables, and directory management.
        - `time`: Provides functions to track and manipulate time, including delays, timestamps, and formatting.
        - `smtplib`: Implements the SMTP protocol for sending emails. Used to connect to mail servers and dispatch notifications.
        - `email.mime`: Supports the creation of MIME-compliant email messages, including plain text, HTML, and attachments. Works in tandem with smtplib for structured email content.
    - External library modules:
        - `black`: Automatically formats Python code to follow PEP 8, ensuring consistency.
        - `mypy`: Performs static type checking to catch type-related bugs before runtime.
        - `pyflakes`: Analyzes Python code for syntax errors and unused imports without executing it.
        - `tabulate`: Formats tabular data into visually appealing tables for a professional terminal display.
        - `cowsay`: Adds playful ASCII art characters to CLI output, enhancing user engagement.
- **Security Notes:**  
  - `credentials.txt` contains plaintext Gmail login (should be secured in future versions)
  - Ensure `.gitignore` excludes sensitive files


## License

This project is licensed under the **MIT License**.  You're free to use, modify, and distribute this software with attribution. See the [`LICENSE`](LICENSE) file for details.

- All standard Python library modules, such as `re`, `json`, `os`, `time`, `smtplib`, and `email.mime`, are upon of Python Software Foundation License (PSFL). 
Legal/Ethical Impact: Open source and permissive. You're free to use, modify, and distribute without restrictions. Ethically safe—commonly used in Python projects. <https://docs.python.org/3/license.html>
- For the external libraries:
    - `cowsay`: GPL-3.0 / Artistic 1.0 (dual-licensed) - <https://github.com/cowsay-org/cowsay/blob/main/LICENSE.txt>
    - `tabulate`: MIT License - <https://github.com/openai/tabulate/blob/master/LICENSE>
    - `black`: MIT License - <https://github.com/psf/black/blob/main/LICENSE>
    - `mypy`: MIT License (with some PSF-licensed files) - <https://github.com/python/mypy/blob/master/LICENSE>
    - `pyflakes`: MIT License - <https://github.com/PyCQA/pyflakes/blob/main/LICENSE>

Files such as `users.json`, `notifications.json`, `sent_notifications.json`, and `credentials.txt`, may have personal data, it needs to comply with Australian Privacy Act or GDPR, especially regarding user consent and data handling. They should never be shared, due to privacy and security risks.

## System Requirements
- Python 3.9+
- Operating System: Windows, macOS, or Linux

## File Structure
- `/project_file`
  - `.venv`: Python virtual environment.
  - `/data`: Contains app data, user input, and operational records.
    - `credentials.txt`: Stores email credentials for sending notifications.
    - `notifications.json`: Queue of user product alert requests.
    - `sent_notifications.json`: Log of dispatched notifications to avoid duplicates.
    - `stock.txt`: Current product stock levels, updated manually.
    - `users.json`: User registration name and email.
  - `/src`: Source code modules for the Notify Me CLI application.
    - `customer_request.py`: Handles user requests for product alerts and processes submissions.
    - `header.py`: Displays the stylized CLI header and welcome message.
    - `main.py`: Application entry point that coordinates all modules.
    - `notifier.py`: Sends email notifications to users when stock is available.
    - `stock_checker.py`: Checks current stock status of tracked items.
    - `stock_monitor.py`: Monitors and compares stock data to detect changes.
    - `user_auth.py`: Manages user authentication, registration logic and email validation.
  - `.gitignore`: Specifies files and folders to exclude from Git.
  - `LICENSE`: Project license outlining usage and distribution terms.
  - `README.md`: Project documentation, setup instructions, and usage info.
  - `requirements-dev.txt`: Development dependencies and tools.
  - `requirements.txt`: Runtime dependencies needed to run the app.

## Setup:
1. Get the Project Files – Download or clone the repository to your computer. 
2. Open the Project Directory – Use the terminal to move into the project's folder:
```bash
cd path/to/project
```
3.  Activate the Virtual Invironment:
 ```bash
 source .venv/bin/activate
 ```
4. Install Dependencies – Install all required packages listed in requirements.txt:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Only if you're developing
```
4. You are ready to start the Application 

## Testing Guide

### 1. Manage Products Stock 
- Add/Delete items in `data/stock.txt` with correct format BEFORE launch the App. 
- Make sure that at least one product has 0 (zero) units in stock, for notification be sent.
- Full stock list will be shown when App launched.

### 2. Launch App
```bash
python3 src/main.py
```
### 3. Register / Log In
- New users: enter your name and email
- Existing users: email is checked against users.json

### 4. Opt-In for Notifications
- Select products you want alerts for when restocked
- Answer if you give the app permission to use your email to send you a notification

### 5. Exit to Monitor
- Exit the App when finish your research
- On exit, the app runs a monitor script to check for stock updates

### 6. Sending notifications
- Following the prompt to update manually products stock in `stock.txt` to trigger notifications.
- Emails will be sent

---
## Future Vision
In future versions, this app will:
- Integrate directly with e-commerce product inventory APIs
- Embed into live product pages with a "Notify Me" button
- Collect and sync customer profiles from the store database
- Monitor inventory in real-time and scale alerts across multiple products

## Troubleshooting
### 1. error: externally-managed-environment - This environment is externally managed
 - 1.1 Make sure you are in Virtual Environment, (.venv). If not create the virtual environment using:
 ```bash
 python3 -m venv .venv
 ```
 - 1.2 And activate it:
 ```bash
 source .venv/bin/activate
 ```
### 2. There are many unexpected `filename.txt:Zone.Identifier` files in my folder. What should I do?
 - 2.1 When you download a file from the internet—like a ZIP, script, or executable— Windows attaches metadata to it indicating its origin . This metadata is stored in a hidden stream named Zone.Identifier. They’re safe to delete if you trust the file’s source. You can remove them using:
 ```bash
 find . -type f -name "*Zone.Identifier" -delete
```
### 3. [Errno 2] No such file or directory
 - 3.1 Make sure you are in the right directory before run main.py
 ```bash
 python3 src/main.py
 ```
### 4. Module Not Found Error:
  - 4.1 Make sure you have installed requirements.txt

### UnicodeDecodeError: 'utf-8' codec can't decode byte in position X
  - 5.1 This usually means the file you’re trying to read contains non-UTF-8 characters. To fix this:
```bash
with open('filename.txt', encoding='latin-1') as f:
    content = f.read()
```
  - 5.2 Alternatively, inspect the file's encoding with a tool like chardet to determine the correct codec:
```bash 
pip install chardet
chardet filename.txt
```