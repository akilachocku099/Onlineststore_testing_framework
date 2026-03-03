# Playwright Automation Testing Framework

This project is an end-to-end UI automation framework built using **Python, Playwright, and Pytest**.  
It automates the testing of an online grocery store application.

Website under test:  
https://rahulshettyacademy.com/seleniumPractise/#/

---

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)

---

## Project Structure

OnlineStore_Testing_Framework/

pages/  
&nbsp;&nbsp;homepage.py  
&nbsp;&nbsp;checkout_page.py  

tests/  
&nbsp;&nbsp;test_search.py  
&nbsp;&nbsp;test_cart.py  
&nbsp;&nbsp;test_checkout.py  

conftest.py  
pytest.ini  
requirements.txt  
README.md  

---

## Test Scenarios Covered

### Search Functionality
- Verify product search
- Verify invalid search returns no results

### Cart Functionality
- Add product to cart
- Add multiple products
- Remove product from cart
- Verify cart count updates correctly

### Checkout Functionality
- Verify products appear in checkout page
- Validate total price calculation
- Complete full checkout flow

---

## Design Pattern Used

**Page Object Model (POM)**

Pages are separated into reusable classes:

- HomePage
- CheckoutPage

This improves maintainability and readability.

---

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd OnlineStore_Testing_Framework