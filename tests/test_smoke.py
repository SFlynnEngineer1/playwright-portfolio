from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_smoke(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url(InventoryPage.URL)
    print("✅ Login smoke test passed")
