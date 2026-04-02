class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        self.page             = page
        self.sort_dropdown    = page.locator('[data-test="product-sort-container"]')
        self.cart_icon        = page.locator('.shopping_cart_link')
        self.cart_badge       = page.locator('.shopping_cart_badge')
        self.inventory_items  = page.locator('.inventory_item')

    def is_loaded(self):
        return self.page.url == self.URL

    def get_item_count(self):
        return self.inventory_items.count()

    def add_item_to_cart_by_name(self, item_name):
        """
        Clicks the 'Add to cart' button for the item matching item_name.
        Sauce Demo's data-test attributes follow the pattern:
          add-to-cart-<kebab-case-item-name>
        e.g. 'Sauce Labs Backpack' → add-to-cart-sauce-labs-backpack
        """
        kebab = item_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="add-to-cart-{kebab}"]').click()

    def remove_item_from_cart_by_name(self, item_name):
        kebab = item_name.lower().replace(" ", "-")
        self.page.locator(f'[data-test="remove-{kebab}"]').click()

    def get_cart_badge_count(self):
        """Returns the integer count shown on the cart badge, or 0 if empty."""
        if self.cart_badge.is_visible():
            return int(self.cart_badge.inner_text())
        return 0

    def go_to_cart(self):
        self.cart_icon.click()

    def sort_by(self, option):
        """
        option values: 'az', 'za', 'lohi', 'hilo'
        """
        self.sort_dropdown.select_option(option)

    def logout(self):
        self.page.locator('#react-burger-menu-btn').click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()

    def add_first_item_to_cart(self):
        """Clicks the Add to cart button for the first item in the list."""
        self.page.locator('[data-test^="add-to-cart"]').first.click()
 
    def get_first_item_name(self):
        """Returns the display name of the first item in the inventory list."""
        return self.page.locator('.inventory_item_name').first.inner_text()

