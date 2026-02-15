import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def setup_driver():
    geckodriver_path = r"F:\It\Python_Ilin_SkyPro\geckodriver.exe"
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_shop_checkout(setup_driver):
    driver = setup_driver

    driver.get("https://www.saucedemo.com/")
    print("Вводим логин и пароль")

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    driver.implicitly_wait(5)
    print("Добавляем товары в корзину")

    backpack_button = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )
    backpack_button.click()

    tshirt_button = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    tshirt_button.click()

    onesie_button = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-onesie"
    )
    onesie_button.click()

    print("Переходим в корзину")
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    print("Заполняем форму")
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Илья")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Ильин")

    zip_field = driver.find_element(By.ID, "postal-code")
    zip_field.send_keys("664000")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    print("Сверяем итоговую сумму")
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_amount = float(total_text.split("$")[1])
    expected_total = 58.29

    assert total_amount == expected_total, (
        f"Ошибка! Ожидалось: ${expected_total}, но получилось: ${total_amount}"
    )

    print(f"Тест пройден! Итоговая сумма: ${total_amount}")
