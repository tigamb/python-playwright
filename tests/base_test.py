from pages.cart_page import CartPage
from pages.item_page import InventoryPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class BaseTest:
    login_page: LoginPage
    products_page: ProductsPage
    item_page: InventoryPage
    cart_page: CartPage
