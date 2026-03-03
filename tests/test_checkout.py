from playwright.sync_api import expect
import pytest

def test_product_exists(home,checkout):
    home.search_product("Carrot")
    home.add_first_product_to_cart()
    home.search_product("Brocolli")
    home.add_first_product_to_cart()
    home.open_cart()
    home.proceed_to_checkout()
    assert checkout.checkcart_items(2,["Carrot","Brocolli"]), "Expected 'Carrot' and 'Brocolli' in cart items, but they were not found"

def test_check_product_price(home,checkout):
    home.search_product("Carrot")
    home.add_first_product_to_cart()
    home.search_product("Brocolli")
    home.add_first_product_to_cart()
    home.open_cart()
    home.proceed_to_checkout()
    total = checkout.total_amount.inner_text()
    prices = checkout.total_amount_value()
    calculated_total = sum(prices)
    assert calculated_total == float(total.replace("₹", "")), f"Expected total {calculated_total}, but got {total}"

def test_complete_checkout_flow(home, checkout):
    # Add product
    home.search_product("Carrot")
    home.add_first_product_to_cart()

    # Go to checkout
    home.open_cart()
    home.proceed_to_checkout()

    # Place order
    checkout.place_order()
    checkout.select_country("India")
    checkout.accept_terms()
    checkout.confirm_order()

    from playwright.sync_api import expect
    expect(checkout.page.locator("text=Thank you")).to_be_visible()