import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_complete_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    inventory_page.add_first_item_to_cart()

    inventory_page.go_to_cart()

    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0

    cart_page.proceed_to_checkout()

    checkout_page.fill_checkout_info("Илья", "Ильин", "664000")
    checkout_page.continue_checkout()

    total_price = checkout_page.get_total_price()
    assert total_price is not None
    print(f"Итоговая стоимость: {total_price}")
