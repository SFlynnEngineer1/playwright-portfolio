class CheckoutPage:

    URL_STEP_ONE = "https://www.saucedemo.com/checkout-step-one.html"
    URL_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page):
        self.page = page

        # Step One — Information form
        self.first_name_field = page.locator('[data-test="firstName"]')
        self.last_name_field  = page.locator('[data-test="lastName"]')
        self.zip_code_field   = page.locator('[data-test="postalCode"]')
        self.continue_button  = page.locator('[data-test="continue"]')
        self.cancel_button    = page.locator('[data-test="cancel"]')
        self.error_message    = page.locator('[data-test="error"]')

        # Step Two — Summary
        self.finish_button    = page.locator('[data-test="finish"]')
        self.subtotal_label   = page.locator('.summary_subtotal_label')
        self.tax_label        = page.locator('.summary_tax_label')
        self.total_label      = page.locator('.summary_total_label')

    # ── Step One methods ──────────────────────────────────────────────

    def fill_information(self, first_name, last_name, zip_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_code_field.fill(zip_code)
        self.continue_button.click()

    def is_step_one_loaded(self):
        return self.page.url == self.URL_STEP_ONE

    def get_error_message(self):
        return self.error_message.inner_text()

    def is_error_visible(self):
        return self.error_message.is_visible()

    # ── Step Two methods ──────────────────────────────────────────────

    def is_step_two_loaded(self):
        return self.page.url == self.URL_STEP_TWO

    def get_subtotal_text(self):
        return self.subtotal_label.inner_text()

    def get_total_text(self):
        return self.total_label.inner_text()

    def finish_order(self):
        self.finish_button.click()

