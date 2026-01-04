import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from playwright.sync_api import expect



class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    __TITLE = '.login_logo'
    __USERNAME_PLACEHOLDER = '[placeholder="Username"]' # getAttribute
    __PASSWORD_PLACEHOLDER = '[placeholder="Password"]' #
    __USER_NAME = '#user-name'
    __PASSWORD = '#password'
    __LOGIN_BTN = '#login-button'
    __ERROR_MESSAGE = '[data-test="error"]' # .error-message-container.error

    def assert_login_page_text_soft_assert(self, expected: dict):
        errors = []

        if self.get_text(self.__TITLE).strip() != expected["title"]:
            errors.append("Title text mismatch")

        if self.get_attribute(self.__USER_NAME, "placeholder").strip() != expected["username_hint"]:
            errors.append("Username placeholder mismatch")

        if self.get_attribute(self.__PASSWORD, "placeholder").strip() != expected["password_hint"]:
            errors.append("Password placeholder mismatch")

        if self.get_attribute(self.__LOGIN_BTN, "value").strip() != expected["login_btn"]:
            errors.append("Login button text mismatch")

        assert not errors, "\n".join(errors)


    def assert_login_page_text(self, title, username_hint, password_hint, login_btn: str):
        assert title ==  self.get_text(self.__TITLE)
        assert username_hint == self.get_attribute(self.__USER_NAME, 'placeholder')
        assert password_hint == self.get_attribute(self.__PASSWORD, 'placeholder')
        assert login_btn == self.get_attribute(self.__LOGIN_BTN,'value')

    @allure.step('Compare main screen text, title: {title} user_hint: {username_hint} pass_hint: {password_hint} login_btn_text {login_btn}')
    def assert_login_page_text_hard_assert(
            self,
            title: str,
            username_hint: str,
            password_hint: str,
            login_btn: str
    ):
        actual_title = self.get_text(self.__TITLE).strip()
        actual_username_hint = self.get_attribute(self.__USER_NAME, "placeholder").strip()
        actual_password_hint = self.get_attribute(self.__PASSWORD, "placeholder").strip()
        actual_login_btn = self.get_attribute(self.__LOGIN_BTN, "value").strip()

        assert actual_title == title, (
            f"\n[Login Page] Title mismatch"
            f"\nExpected: '{title}'"
            f"\nActual:   '{actual_title}'"
        )

        assert actual_username_hint == username_hint, (
            f"\n[Login Page] Username placeholder mismatch"
            f"\nExpected: '{username_hint}'"
            f"\nActual:   '{actual_username_hint}'"
        )

        assert actual_password_hint == password_hint, (
            f"\n[Login Page] Password placeholder mismatch"
            f"\nExpected: '{password_hint}'"
            f"\nActual:   '{actual_password_hint}'"
        )

        assert actual_login_btn == login_btn, (
            f"\n[Login Page] Login button text mismatch"
            f"\nExpected: '{login_btn}'"
            f"\nActual:   '{actual_login_btn}'"
        )

    @allure.step('login with username: {user_name} and password: {password}')
    def enter_user_name_and_password(self, user_name, password):
        self.fill_text(self.__USER_NAME, user_name)
        self.fill_text(self.__PASSWORD, password)

    @allure.step('Click login button')
    def click_login_btn(self):
        self.click_on_element(self.__LOGIN_BTN)

    @allure.step('Get error message while using invalid data')
    def get_error_message(self):
        #return self.page.locator(self.__ERROR_MESSAGE).inner_text()
        return self.get_text(self.__ERROR_MESSAGE)

    @allure.step('Assert error message while using invalid data')
    def assert_error_message(self, expected: str):
        actual = self.get_error_message()
        assert actual == expected, (
            f"\nExpected error message:\n'{expected}'"
            f"\nActual error message:\n'{actual}'"
        )

    def assert_error_message_contains(self, expected_partial: str):
        actual = self.get_error_message()
        assert expected_partial in actual, (
            f"\nExpected error message to contain:\n'{expected_partial}'"
            f"\nActual error message:\n'{actual}'"
        )