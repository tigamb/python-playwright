import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header import HeaderComponent as HC, HeaderComponent


class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.__header = HeaderComponent(page)


    __ITEM = ".inventory_item"
    __ITEM_TITLE = '.inventory_item_name'
    __ITEM_DESCRIPTION = '.inventory_item_desc'
    __ITEM_PRICE = '.inventory_item_price'
    __ADD_TO_CART_BTN = '.btn_primary.btn_small.btn_inventory'
    __SORT_BTN = '.active_option'
    __FILTER = '.product_sort_container'

    # TODO: handle alert
    # TODO: add method to the sort
    # TODO: use SELECT for the sort -  locator -->  .product_sort_container



    # החזרת כל שמות המוצרים
    @allure.step('Return all products title as list')
    def get_all_product_titles(self) -> list[str]:
        return self.page.locator(self.__ITEM_TITLE).all_inner_texts()

    # החזרת כל התיאורים של המוצרים
    @allure.step('Return all products description as list')
    def get_all_product_desc(self) -> list[str]:
        return self.page.locator(self.__ITEM_DESCRIPTION).all_inner_texts()


    # החזרת מספר המוצרים
    @allure.step('Get total item count')
    def get_products_count(self) -> int:
        return self.page.locator(self.__ITEM).count()

    # הוספה לעגלה לפי שם מוצר
    @allure.step('Add an item using product name {product_name}')
    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(self.__ITEM).filter(has_text=product_name)
        product.locator(self.__ADD_TO_CART_BTN).click()

    # קבלת מחיר של מוצר לפי שם
    @allure.step('Get item price using product name {product_name}')
    def get_product_price(self, product_name: str) -> str:
        product = self.page.locator(self.__ITEM).filter(has_text=product_name)
        return product.locator(self.__ITEM_PRICE).inner_text()

    @allure.step('Filter using item name: {value}')
    def filter_list(self, value):
        self.select_dropdown_option(self.__FILTER,value)

    @allure.step('Print page title')
    def print_current_title(self):
        print(self.__header.get_current_page_title())


