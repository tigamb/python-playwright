from playwright.sync_api import Page

from pages.base_page import BasePage


class HeaderComponent(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    __HAMBURGER = '#react-burger-menu-btn'
    __MAIN_TITLE = '.header_label>.app_logo'
    __CART_ICON = '#shopping_cart_container'
    __PAGE_TITLE = '.title'

    # TODO: method to open hamburger menu
    # TODO: method to print the title
    # TODO: method to click cart icon
    # TODO: add more methods....



    def get_current_page_title(self) -> str:
        self.highlight(self.__PAGE_TITLE, "orange")
        return self.page.text_content(self.__PAGE_TITLE)