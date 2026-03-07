from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class LoginPage(BasePage):
    """Страница авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container']")

    @allure.step("Ввод имени пользователя '{username}'")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле ввода.

        Args:
            username (str): имя пользователя
        """
        self.input_text(self.USERNAME_INPUT, username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле ввода.

        Args:
            password (str): пароль
        """
        self.input_text(self.PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки входа")
    def click_login(self) -> None:
        """Кликает кнопку входа."""
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Авторизация с учётными данными '{username}' / '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию с указанными учётными данными.

        Args:
            username (str): имя пользователя
            password (str): пароль
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке.

        Returns:
            str: текст сообщения
        """
        return self.find_element(self.ERROR_MESSAGE).text
