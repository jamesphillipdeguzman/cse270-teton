# CSE270 – Teton Project

## 📌 Overview

The Teton Project is a web application developed and tested as part of CSE270.  
This project focuses on front-end navigation, form validation, and automated smoke testing using Selenium and Pytest.

The site includes multiple pages such as:

- Home Page
- Directory Page
- Join Page
- Admin Page (Login)

The project demonstrates functional UI testing, navigation verification, and validation testing.

---

## 🎯 Project Objectives

- Verify correct page routing and navigation
- Validate login functionality (positive and negative cases)
- Test dynamic error messages
- Perform smoke testing on key pages
- Automate UI testing using Selenium WebDriver with Pytest

---

## 🧪 Automated Testing

The project includes automated smoke tests written in Python using:

- Selenium WebDriver
- Pytest

### Smoke Tests Cover:

- Home page loads successfully
- Directory page is accessible
- Join page navigation works
- Admin page loads properly
- Invalid login shows error message

---

## ⚙️ Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Django Web Service
- Selenium WebDriver
- Pytest

---

## 🚀 How to Run the Project Locally

1. Open latest version 1.6
2. Navigate to cse270
3. Go into directorydata_service
4. Type Run manage.py runserver in your terminal
5. Select index.html
6. Click Go Live

Result: Website opens in localhost 

[Open Teton frontend version 1.6](http://127.0.0.1:5501/cse270/teton/1.6/index.html)

```bash
python -m http.server 5501
