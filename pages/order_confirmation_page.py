class OrderConfirmationPage:

    URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page):
        self.page             = page
        self.confirmation_header = page.locator('.complete-header')
        self.confirmation_text   = page.locator('.complete-text')
        self.back_home_button    = page.locator('[data-test="back-to-products"]')

    def is_loaded(self):
        return self.page.url == self.URL

    def get_confirmation_header(self):
        return self.confirmation_header.inner_text()

    def get_confirmation_text(self):
        return self.confirmation_text.inner_text()

    def go_back_home(self):
        self.back_home_button.click()

