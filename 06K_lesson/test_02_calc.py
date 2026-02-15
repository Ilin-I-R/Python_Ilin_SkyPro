import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_driver():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 60)
    yield driver, wait
    driver.quit()


def test_calculator(setup_driver):
    driver, wait = setup_driver

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_field = wait.until(
        EC.presence_of_element_located((By.ID, "delay"))
    )
    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(
        By.XPATH,
        "//span[contains(@class, 'operator') and text()='+']"
    ).click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "spinner")))
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    result_screen = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
    )
    assert result_screen.text == "15", (
        f"Ожидался результат 15, но получен {result_screen.text}"
    )

    print("Тест пройден успешно! Результат равен 15.")
