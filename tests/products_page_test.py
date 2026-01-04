import allure
import pytest

from tests.base_test_04012026 import BaseTest
from utils.yaml_loader import TestDataLoader as TD


class TestProducts(BaseTest):

    @pytest.mark.parametrize("data", TD.get("login", "positive"), ids=lambda d: d["name"])
    def test_login_with_correct_data(self, data):
        with allure.step('Login page steps'):
            self.login_page.enter_user_name_and_password(data['username'], data['password'])
            self.login_page.click_login_btn()

    @allure.description('Print products page title and also print another text')
    def test_assert_something(self):
        with allure.step('Products page steps'):
            self.products_page.print_current_title()
            print('\nYou are inside products page')