import pytest
import allure
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


@allure.feature("Покупка товаров")
@allure.description(
    "Полный сценарий покупки: "
    "авторизация → добавление товара → оформление заказа"
)
@allure.title("Тест: Полный процесс покупки товара на saucedemo")
@allure.severity(allure.severity_level.BLOCKER)
def test_complete_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открытие главной страницы saucedemo"):
        driver.get("https://www.saucedemo.com/")

    with allure.step(
        "Авторизация с учётными данными standard_user / secret_sauce"
    ):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверка успешной авторизации"):
        assert "inventory.html" in driver.current_url

    with allure.step("Добавление первого товара в корзину"):
        inventory_page.add_first_item_to_cart()

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Проверка наличия товаров в корзине"):
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) > 0

    with allure.step("Продолжение оформления заказа"):
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение информации для доставки"):
        checkout_page.fill_checkout_info("Илья", "Ильин", "664000")
        checkout_page.continue_checkout()

    with allure.step("Проверка итоговой стоимости"):
        total_price = checkout_page.get_total_price()
        assert total_price is not None
        print(f"Итоговая стоимость: {total_price}")
