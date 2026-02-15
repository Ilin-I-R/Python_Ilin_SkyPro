import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_driver():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


def test_fill_form(setup_driver):
    driver, wait = setup_driver

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    first_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    first_name_field.send_keys("Иван")

    last_name_field = driver.find_element(By.NAME, "last-name")
    last_name_field.send_keys("Петров")

    address_field = driver.find_element(By.NAME, "address")
    address_field.send_keys("Ленина, 55-3")

    email_field = driver.find_element(By.NAME, "e-mail")
    email_field.send_keys("test@skypro.com")

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.send_keys("+7985899998787")

    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("Москва")

    country_field = driver.find_element(By.NAME, "country")
    country_field.send_keys("Россия")

    job_position_field = driver.find_element(By.NAME, "job-position")
    job_position_field.send_keys("QA")

    company_field = driver.find_element(By.NAME, "company")
    company_field.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    )
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_classes = zip_code_field.get_attribute("class")
    assert "alert-danger" in zip_code_classes, (
        "Zip code должен быть красным, но цвет другой"
    )

    other_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in other_fields:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, (
            f"Поле {field_id} должно быть зелёным, но цвет другой"
        )

    print("Все проверки пройдены успешно!")
