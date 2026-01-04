# 🎭 Python Playwright Automation Framework

A comprehensive test automation framework built with **Playwright** and **Python**, featuring Page Object Model (POM) design pattern, data-driven testing, and detailed reporting with Allure.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running Tests](#-running-tests)
- [Allure Reports](#-allure-reports)
- [Page Object Model](#-page-object-model)

## ✨ Features

- 🎯 **Page Object Model (POM)** - Maintainable and scalable test architecture
- 📊 **Data-Driven Testing** - YAML-based test data management
- 📸 **Automatic Screenshots** - Captures screenshots on test failures
- 📈 **Allure Reports** - Beautiful and detailed test reports
- 🔧 **Reusable Components** - Common page components for DRY principles
- ⚡ **Parallel Execution** - Fast test execution with pytest-xdist
- 🛠️ **Configurable** - Easy configuration through INI and YAML files

## 📂 Project Structure

```
python-playwright/
├── data/
│   ├── config.ini              # Configuration settings
│   └── test_data.yaml          # Test data for data-driven tests
├── pages/
│   ├── components/
│   │   ├── __init__.py
│   │   └── base_page.py        # Base page with common methods
│   ├── cart_page.py            # Shopping cart page object
│   ├── checkout_step1.py       # Checkout step 1 page object
│   ├── checkout_step2.py       # Checkout step 2 page object
│   ├── checkout_step3.py       # Checkout step 3 page object
│   ├── item_page.py            # Product item page object
│   ├── login_page.py           # Login page object
│   └── products_page.py        # Products listing page object
├── tests/
│   ├── __init__.py
│   ├── base_test.py            # Base test class with fixtures
│   ├── conftest.py             # Pytest configuration and fixtures
│   ├── products_page_test.py   # Products page test suite
│   ├── test_login_page.py      # Login functionality tests
│   └── test_login_page_with_logs.py  # Login tests with logging
├── utils/
│   ├── __init__.py
│   ├── config.py               # Configuration loader
│   ├── yaml_loader.py          # YAML data loader
│   └── yaml_loader_OLD.py      # Legacy YAML loader
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Project dependencies
└── README.md                   # This file
```

## 🔧 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tigamb/python-playwright.git
   cd python-playwright
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## ⚙️ Configuration

### config.ini
Edit `data/config.ini` to configure your test environment:

```ini
[base]
url = https://your-app-url.com
browser = chromium
headless = false
```

### test_data.yaml
Manage your test data in `data/test_data.yaml`:

```yaml
users:
  valid_user:
    username: standard_user
    password: secret_sauce
  invalid_user:
    username: invalid_user
    password: wrong_password
```

## 🚀 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test file:
```bash
pytest tests/test_login_page.py
```

### Run tests with specific marker:
```bash
pytest -m smoke
```

### Run tests in headless mode:
```bash
pytest --headed=false
```

### Run tests in parallel:
```bash
pytest -n auto
```

### Run with specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

## 📊 Allure Reports

### Generate and view Allure report:

1. **Run tests with Allure:**
   ```bash
   pytest --alluredir=allure-results
   ```

2. **Generate and open report:**
   ```bash
   allure serve allure-results
   ```

3. **Generate static report:**
   ```bash
   allure generate allure-results --clean -o allure-report
   ```

### Features in Allure Report:
- ✅ Test execution status
- 📸 Screenshots on failures
- 🌐 Browser and environment information
- ⏱️ Execution time and history
- 📋 Test steps and logs

## 🎨 Page Object Model

The framework uses POM design pattern for better maintainability:

### Base Page (`pages/components/base_page.py`)
Contains common methods used across all pages:
- Navigation
- Element interactions
- Waits and assertions

### Page Objects
Each page has its own class with locators and methods:
- `login_page.py` - Login functionality
- `products_page.py` - Product listing and filtering
- `cart_page.py` - Shopping cart operations
- `checkout_step1.py/2.py/3.py` - Checkout flow

### Example Usage:
```python
from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("username", "password")
    assert login_page.is_logged_in()
```

## 🧪 Writing Tests

Tests inherit from `BaseTest` class which provides common fixtures:

```python
from tests.base_test import BaseTest

class TestProducts(BaseTest):
    def test_product_page(self):
        # Test implementation
        pass
```

## 📝 Test Data Management

Use YAML files for data-driven testing:

```python
from utils.yaml_loader import load_test_data

test_data = load_test_data('test_data.yaml')
username = test_data['users']['valid_user']['username']
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Happy Testing! 🎭✨**
