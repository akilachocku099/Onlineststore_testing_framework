from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.page = page

        # Locators
        self.product_rows = page.locator(".cartTable tbody tr")
        self.total_amount = page.locator(".totAmt")
        self.place_order_button = page.locator("button:has-text('Place Order')")
        self.country_input =page.locator(".wrapperTwo select")
        self.country_suggestion = page.locator(".suggestions li")
        self.terms_checkbox = page.locator(".chkAgree")
        self.proceed_button = page.locator("button:has-text('Proceed')")
        self.success_message = page.locator(".alert-success")

    def cart_items(self):
        return self.product_rows.all_text_contents()
    def checkcart_items(self,n,names):
        count=self.product_rows.count()
        if count!=n:
            return False
        for i in range(count):
            item = self.product_rows.nth(i)
            name = item.locator(".product-name").inner_text()
            if not any(expected in name for expected in names):
                return False
        return True
    def total_amount_value(self):
        count=self.product_rows.count()
        prices=[]
        names=[]
        for i in range(count):
            item = self.product_rows.nth(i)
            name = item.locator(".product-name").inner_text()
            price_part = item.locator(".amount").last.inner_text()

            if name not in names:
                price=float(price_part.replace("₹", ""))
                prices.append(price)
                names.append(name)
        return prices
    
    def place_order(self):
        self.place_order_button.click()
        self.page.wait_for_selector(".wrapperTwo select")
    def select_country(self, country_name):
        self.page.locator(".wrapperTwo select").select_option(country_name)
        # Wait until the dropdown actually reflects the selected value
        expect(self.page.locator(".wrapperTwo select")).to_have_value(country_name, timeout=5000)

    def accept_terms(self):
        self.terms_checkbox.check()
    def confirm_order(self):
        self.proceed_button.click()