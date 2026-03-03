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
  homepage.py  
  checkout_page.py  

tests/  
  test_search.py  
  test_cart.py  
  test_checkout.py  

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
git clone https://github.com/akilachocku099/Onlineststore_testing_framework.git
cd OnlineStore_Testing_Framework
pip install -r requirements.txt
pytest

---

## Future Improvements

This framework can be enhanced further with:

- **CI/CD Integration**  
  Set up GitHub Actions or Jenkins pipelines to run tests automatically on every commit.

- **Test Reporting**  
  Add HTML or Allure reports for better visualization of test results.

- **Cross-Browser Testing**  
  Extend Playwright tests to run across Chrome, Firefox, and WebKit for broader coverage.

- **Environment Configurations**  
  Support multiple environments (dev, staging, production) with configurable base URLs.

- **Additional Test Coverage**  
  Expand scenarios to include login, promotions, order history, and error handling.

- **Dockerization**  
  Containerize the framework for consistent execution across different systems.

---