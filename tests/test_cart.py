import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

ITEM_COUNTS = [1, 2, 3]


def test_add_single_item_to_cart(inventory_page):
    inventory_page.add_first_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.parametrize("count", ITEM_COUNTS)
def test_add_multiple_items_updates_badge(inventory_page, count):
    for _ in range(count):
        inventory_page.add_first_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text(str(count))


def test_cart_badge_absent_when_empty(inventory_page):
    expect(inventory_page.cart_badge).not_to_be_visible()


def test_item_appears_in_cart(inventory_page):
    item_name = inventory_page.get_first_item_name()
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart = CartPage(inventory_page.page)
    expect(cart.first_item_name).to_have_text(item_name)


def test_remove_item_from_cart(inventory_page):
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    cart = CartPage(inventory_page.page)
    cart.remove_first_item()
    expect(cart.item_list).to_have_count(0)
    expect(inventory_page.cart_badge).not_to_be_visible()


def test_continue_shopping_returns_to_inventory(inventory_page):
    inventory_page.go_to_cart()
    cart = CartPage(inventory_page.page)
    cart.continue_shopping()
    expect(inventory_page.page).to_have_url(InventoryPage.URL)

