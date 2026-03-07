from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Базовый класс для всех страниц.
        Содержит общие методы взаимодействия с элементами."""

    def __init__(self, driver):
        """
        Инициализация страницы.

        Args:
            driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента по локатору {locator}")
    def find_element(self, locator: tuple) -> object:
        """
        Ожидает появления элемента и возвращает его.

        Args:
            locator (tuple): локатор элемента в формате (By.METHOD, "value")

        Returns:
            WebElement: найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator: tuple) -> None:
        """
        Находит элемент и кликает по нему.

        Args:
            locator (tuple): локатор элемента
        """
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def input_text(self, locator: tuple, text: str) -> None:
        """
        Вводит текст в указанное поле.

        Args:
            locator (tuple): локатор поля ввода
            text (str): текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
