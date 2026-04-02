import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

INVALID_CREDENTIALS = [
    ("locked_out_user",  "secret_sauce",  "Epic sadface: Sorry, this user has been locked out."),
    ("standard_user",    "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
    ("",                 "secret_sauce",  "Epic sadface: Username is required"),
    ("standard_user",    "",              "Epic sadface: Password is required"),
]


def test_valid_login(login_page):
    login_page.navigate()
    login_page.login(VALID_USER, VALID_PASS)
    expect(login_page.page).to_have_url(InventoryPage.URL)


def test_logout(login_page):
    login_page.navigate()
    login_page.login(VALID_USER, VALID_PASS)
    inventory = InventoryPage(login_page.page)
    inventory.logout()
    expect(login_page.page).to_have_url(LoginPage.URL)


@pytest.mark.parametrize("username, password, expected_error", INVALID_CREDENTIALS)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.navigate()
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)


def test_cannot_access_inventory_without_login(page):
    page.goto(InventoryPage.URL)
    expect(page).to_have_url(LoginPage.URL)

