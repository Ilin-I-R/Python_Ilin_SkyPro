import pytest
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


def test_calculator_functionality(setup_driver):
    page = PageObject(setup_driver)
    page.open()
    page.set_delay(45)
    page.click_button_7()
    page.click_plus()
    page.click_button_8()
    page.click_equals()
    page.wait_for_calculation_complete()
    result = page.get_result()
    assert result == "15", f"Ожидаемый результат 15, но получен {result}"
