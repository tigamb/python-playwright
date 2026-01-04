from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header import HeaderComponent


class CheckoutStep2(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = HeaderComponent(page)


    def print_current_title(self):
        print(self.__header.get_current_page_title())