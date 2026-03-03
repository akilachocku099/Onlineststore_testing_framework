from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator(".search-keyword")
        self.add_buttons = page.locator(".product-action > button")
        self.cart_count = page.locator(".cart-info strong").first
        self.proceed_button = page.locator("button:has-text('Proceed')")

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    def search_product(self, product_name: str):
        self.search_input.fill("") 
        self.search_input.fill(product_name)
        # Wait until the product list updates
        expect(self.page.locator(".products-wrapper .product")).to_have_count(1, timeout=5000)

    def open_cart(self):
        self.page.locator(".cart-icon").click()
        # Wait until the cart preview is visible
        expect(self.page.locator(".cart-preview")).to_be_visible(timeout=5000)

    def remove_product_by_name(self, product_name: str):
        cart_items = self.page.locator(".cart-item")

        count = cart_items.count()

        for i in range(count):
            item = cart_items.nth(i)

            name = item.locator(".product-name").inner_text()

            if product_name in name:
                item.locator(".product-remove").click()
                self.page.wait_for_timeout(1000)
                break
    def check_product_exists(self, product_name: str):
        return self.page.locator(".cart-item",has_text=product_name).count()>0
    def add_first_product_to_cart(self):
        self.add_buttons.first.click()
    def get_search_results(self):
        products = self.page.locator(".products-wrapper .product")
        self.page.locator(".products-wrapper .product").first.wait_for()
        return products.all_text_contents()

    def get_cart_count(self):
        expect(self.cart_count).not_to_have_text("0")
        return self.cart_count

    def get_price_from_cart(self):
        cart_items = self.page.locator(".cart-item")

        count = cart_items.count()
        prices=[]
        names=[]
        for i in range(count):
            item = cart_items.nth(i)

            name = item.locator(".product-name").inner_text()
            price_part = item.locator(".product-price").inner_text()

            if name not in names:
                price=float(price_part.replace("₹", ""))
                prices.append(price)
                names.append(name)
        return  prices
    def proceed_to_checkout(self):
        self.proceed_button.click()
        # Wait until checkout table rows are visible
        self.page.wait_for_selector(".cartTable tbody tr", timeout=5000)
