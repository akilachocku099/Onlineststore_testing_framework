from playwright.sync_api import expect
import pytest

@pytest.mark.parametrize("product", ["Carrot", "Brocolli", "Beetroot"])
def test_add_product(home,product):
    home.search_product(product)
    home.add_first_product_to_cart()
    expect(home.get_cart_count()).to_have_text("1")

def test_add_veg_to_cart(home):
    home.search_product("Carrot")
    home.add_first_product_to_cart()
    home.search_product("Brocolli")
    home.add_first_product_to_cart()
    expect(home.get_cart_count()).to_have_text("2")

def test_remove_product(home):
    home.search_product("Carrot")
    home.add_first_product_to_cart()
    home.search_product("brocolli")
    home.add_first_product_to_cart()
    home.open_cart()
    home.remove_product_by_name("Carrot")
    assert  not home.check_product_exists("Carrot") 
    expect(home.get_cart_count()).to_have_text("1")