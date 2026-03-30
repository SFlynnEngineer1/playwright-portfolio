import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_smoke():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False so you can watch
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(page)
        assert inventory.is_loaded(), f"Expected inventory URL, got: {page.url}"
        print("✅ Login smoke test passed")

        browser.close()

