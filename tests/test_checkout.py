import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage

VALID_CUSTOMER = {"first": "Jane", "last": "Tester", "zip": "94105"}

INVALID_CUSTOMER_INFO = [
    ("",      "Tester", "94105", "Error: First Name is required"),
    ("Jane",  "",       "94105", "Error: Last Name is required"),
    ("Jane",  "Tester", "",      "Error: Postal Code is required"),
]


@pytest.fixture()
def cart_with_item(inventory_page):
    """Adds one item to the cart and navigates to checkout step one."""
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart = CartPage(inventory_page.page)
    cart.proceed_to_checkout()
    return CheckoutPage(inventory_page.page)


def test_full_checkout_happy_path(cart_with_item):
    checkout = cart_with_item
    checkout.fill_information(
        VALID_CUSTOMER["first"],
        VALID_CUSTOMER["last"],
        VALID_CUSTOMER["zip"]
    )

    expect(checkout.page).to_have_url(CheckoutPage.URL_STEP_TWO)
    expect(checkout.subtotal_label).to_be_visible()
    expect(checkout.total_label).to_be_visible()

    checkout.finish_order()

    confirm = OrderConfirmationPage(checkout.page)
    expect(confirm.page).to_have_url(OrderConfirmationPage.URL)
    expect(confirm.confirmation_header).to_have_text("Thank you for your order!")


@pytest.mark.parametrize("first, last, zip_code, expected_error", INVALID_CUSTOMER_INFO)
def test_checkout_validation_errors(cart_with_item, first, last, zip_code, expected_error):
    checkout = cart_with_item
    checkout.fill_information(first, last, zip_code)
    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_have_text(expected_error)


def test_order_summary_shows_before_finish(cart_with_item):
    checkout = cart_with_item
    checkout.fill_information(
        VALID_CUSTOMER["first"],
        VALID_CUSTOMER["last"],
        VALID_CUSTOMER["zip"]
    )

    subtotal_text = checkout.get_subtotal_text()
    total_text = checkout.get_total_text()

    assert "$" in subtotal_text, f"Expected dollar sign in subtotal, got: {subtotal_text}"
    assert "$" in total_text, f"Expected dollar sign in total, got: {total_text}"


def test_back_home_after_order(cart_with_item):
    checkout = cart_with_item
    checkout.fill_information(
        VALID_CUSTOMER["first"],
        VALID_CUSTOMER["last"],
        VALID_CUSTOMER["zip"]
    )
    checkout.finish_order()

    confirm = OrderConfirmationPage(checkout.page)
    confirm.go_back_home()
    expect(confirm.page).to_have_url(InventoryPage.URL)

