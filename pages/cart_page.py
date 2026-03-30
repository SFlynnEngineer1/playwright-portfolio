class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page):
        self.page              = page
        self.cart_items        = page.locator('.cart_item')
        self.checkout_button   = page.locator('[data-test="checkout"]')
        self.continue_shopping = page.locator('[data-test="continue-shopping"]')

    def is_loaded(self):
        return self.page.url == self.URL

    def get_item_count(self):
        return self.cart_items.count()

    def get_item_names(self):
        return self.page.locator('.inventory_item_name').all_inner_texts()

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping.click()

