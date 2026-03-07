from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageObject:
    """Класс для работы с калькулятором на тестовой странице."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        Args:
            driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.spinner = (By.ID, "spinner")

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Установка задержки {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку калькуляции.

        Args:
            seconds (int): количество секунд задержки
        """
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажатие кнопки 7")
    def click_button_7(self) -> None:
        """Кликает кнопку с цифрой 7."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_7)
        )
        button.click()

    @allure.step("Нажатие кнопки 8")
    def click_button_8(self) -> None:
        """Кликает кнопку с цифрой 8."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_8)
        )
        button.click()

    @allure.step("Нажатие кнопки +")
    def click_plus(self) -> None:
        """Кликает кнопку сложения."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button.click()

    @allure.step("Нажатие кнопки =")
    def click_equals(self) -> None:
        """Кликает кнопку равно."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button.click()

    @allure.step("Получение результата вычисления")
    def get_result(self) -> str:
        """
        Получает результат вычисления.

        Returns:
            str: текст результата
        """
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.result_screen)
        )
        return result_element.text

    @allure.step("Ожидание завершения вычисления")
    def wait_for_calculation_complete(self) -> None:
        """Ожидает исчезновения индикатора загрузки."""
        self.wait.until(
            EC.invisibility_of_element_located(self.spinner)
        )
