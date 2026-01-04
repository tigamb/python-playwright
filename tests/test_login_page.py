import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest
from utils.yaml_loader import TestDataLoader as TD



@allure.epic('Security')
@allure.feature('Login')
class TestLogin(BaseTest):

    @allure.severity(Severity.MINOR)
    @allure.description('Compare main screen text - title, username hint, password hint and login button')
    @allure.title('Main screen text')
    @pytest.mark.order(1)
    @pytest.mark.parametrize("data", TD.get("login", "main screen text"), ids=lambda d: d["name"])
    def test_main_screen_text_compare(self, data):
        self.login_page.assert_login_page_text(
            data['title'],
            data['username_placeholder'],
            data['password_placeholder'],
            data['login_button'])

    @allure.severity(Severity.NORMAL)
    @pytest.mark.order(2)
    @pytest.mark.parametrize("data", TD.get("login", "main screen text"), ids=lambda d: d["name"])
    def test_main_screen_text_hard_compare(self, data):
        self.login_page.assert_login_page_text_hard_assert(
            data['title'],
            data['username_placeholder'],
            data['password_placeholder'],
            data['login_button'])


    @pytest.mark.order(3)
    @pytest.mark.parametrize("data", TD.get("login", "main screen text"), ids=lambda d: d["name"])
    def main_screen_text_soft_compare(self, data):
        self.login_page.assert_login_page_text_soft_assert(data)

    @allure.severity(Severity.CRITICAL)
    @allure.description('Check error message of locked user')
    @allure.title('locked user details')
    @pytest.mark.order(4)
    @allure.story('As a blocked user i want to get an error message')
    @pytest.mark.parametrize("data", TD.get("login", "locked user"), ids=lambda d: d["name"])
    def test_login_with_locked_user_data(self, data):
        self.login_page.enter_user_name_and_password(data['username'], data['password'])
        self.login_page.click_login_btn()
        self.login_page.assert_error_message(data['error'])

    @allure.severity(Severity.CRITICAL)
    @allure.description('Check all error messages on login page')
    @allure.title('Invalid login data')
    @pytest.mark.order(5)
    @allure.story('While using incorrect user and password - i want to get an error message')
    @pytest.mark.parametrize("data", TD.get("login", "negative"), ids=lambda d: d["name"])
    def test_login_with_incorrect_data_and_check_error_messages(self, data):
        self.login_page.enter_user_name_and_password(data['username'], data['password'])
        self.login_page.click_login_btn()
        self.login_page.assert_error_message(data['error'])

    @allure.severity(Severity.BLOCKER)
    @allure.description('Enter correct username and password - moves to products page')
    @allure.title('Valid login data')
    @pytest.mark.order(6)
    @allure.story('When i use a valid username and password i want to move into products page')
    @pytest.mark.parametrize("data", TD.get("login", "positive"), ids=lambda d: d["name"])
    def test_login_with_correct_data(self, data):
        self.login_page.enter_user_name_and_password(data['username'], data['password'])
        self.login_page.click_login_btn()




