import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from page_objects import PageObject


@pytest.fixture
def setup_driver():
    driver_path = "F:/It/Python_Ilin_SkyPro/msedgedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.description("Проверка функциональности калькулятора с задержкой")
@allure.title("Тест: Сложение чисел 7 и 8 с задержкой 45 секунд")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_functionality(setup_driver):
    page = PageObject(setup_driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay(45)

    with allure.step("Ввод чисел и операции: 7 + 8"):
        page.click_button_7()
        page.click_plus()
        page.click_button_8()
        page.click_equals()

    with allure.step("Ожидание результата"):
        page.wait_for_calculation_complete()
        result = page.get_result()

    with allure.step(f"Проверка результата: ожидается 15, получено {result}"):
        assert result == "15", f"Ожидаемый результат 15, но получен {result}"
