from typing import Dict

import allure
import pytest
from playwright.sync_api import Page
import os
from datetime import datetime

from pages.cart_page import CartPage
from pages.item_page import InventoryPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import ConfigReader
from utils.yaml_loader import TestDataLoader as TD


BASE_URL = ConfigReader.read_config('general', 'url')


@pytest.fixture(scope="class", autouse=True)
def setup_page_before_each_class(request, browser):
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    request.cls.page = context.new_page()
    request.cls.page.goto(BASE_URL)
    request.cls.login_page = LoginPage(request.cls.page)
    request.cls.products_page = ProductsPage(request.cls.page)
    request.cls.item_page = InventoryPage(request.cls.page)
    request.cls.cart_page = CartPage(request.cls.page)

    yield

    request.cls.page.close()
    context.close()  # סוגר את ההקשר
    #browser.close()

@pytest.fixture(scope='function', autouse=False)
def setup_page_before_each_function(request, page: Page):
    page.goto(BASE_URL)
    request.cls.login_p = LoginPage(request.cls.page)
    request.cls.products_p = ProductsPage(request.cls.page)
    request.cls.item_p = InventoryPage(request.cls.page)



#@pytest.fixture(scope="function", autouse=True)
def goto(page):
    page.goto(BASE_URL)
    yield
    # time.sleep(100)


#@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True,
    }


#@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict):
    """Fixture to set browser launch arguments.
    Args:
        browser_type_launch_args (dict): Browser type launch arguments.
    Returns:
        dict: Updated browser type launch arguments.
    See Also:
        https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
    """
    return {**browser_type_launch_args, "args": ["--start-maximized"]}


@pytest.fixture(scope="session")
def test_data():
    """
    Load test data once per test session
    """
    return TD.load()


#@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request):
    yield
    if request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(
            body=screenshot,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )



#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     # אנחנו רוצים לצלם רק אחרי שלב ה-call (הרצת הטסט עצמו)
#     if report.when == "call" and report.failed:
#         try:
#             page = item.cls.page
#         except Exception:
#             return
#
#         screenshots_dir = "screenshots"
#         os.makedirs(screenshots_dir, exist_ok=True)
#
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         test_name = item.name.replace("/", "_")
#         file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"
#
#         page.screenshot(path=file_path, full_page=True)
#
#         print(f"\n📸 Screenshot saved to: {file_path}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # אנחנו רוצים לצלם רק אחרי שלב ה-call (הרצת הטסט עצמו)
    if report.when == "call" and report.failed:
        try:
            page = item.cls.page
        except Exception:
            return

        # צילום מסך כ-bytes
        screenshot_bytes = page.screenshot(full_page=True)

        # צירוף ל-Allure
        allure.attach(
            body=screenshot_bytes,
            name=f"screenshot_{item.name}",
            attachment_type=allure.attachment_type.PNG
        )

        # אופציונלי - שמירה גם לקובץ
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = item.name.replace("/", "_")
        file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

        with open(file_path, "wb") as f:
            f.write(screenshot_bytes)

        print(f"\n📸 Screenshot saved to: {file_path}")


# הדפסת משתני סביבה
@pytest.fixture(scope="session", autouse=True)
def save_browser_info(browser):
    yield

    environment_properties = {
        'browser': browser.browser_type.name,
        'browser_version': browser.version
    }

    allure_env_path = os.path.join("allure-results", 'environment.properties')
    os.makedirs("allure-results", exist_ok=True)

    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)