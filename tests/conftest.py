import pytest
from pages.homepage import HomePage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def home(page):
    home = HomePage(page)
    home.navigate()
    return home

@pytest.fixture
def checkout(page):
    return CheckoutPage(page)