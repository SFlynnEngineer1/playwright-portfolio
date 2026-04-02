import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture()
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def logged_in_page(page):
    """Returns a page already authenticated as standard_user."""
    lp = LoginPage(page)
    lp.navigate()
    lp.login("standard_user", "secret_sauce")
    return page


@pytest.fixture()
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)


@pytest.fixture()
def cart_page(logged_in_page):
    return CartPage(logged_in_page)


@pytest.fixture()
def checkout_page(logged_in_page):
    return CheckoutPage(logged_in_page)

