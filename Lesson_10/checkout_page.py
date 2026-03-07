from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Страница оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение информации для оформления заказа")
    def fill_checkout_info(
        self,
        firstname: str,
        lastname: str,
        postalcode: str
    ) -> None:

        """
        Заполняет форму оформления заказа.

        Args:
            firstname (str): имя
            lastname (str): фамилия
            postalcode (str): почтовый индекс
        """
        self.input_text(self.FIRST_NAME_INPUT, firstname)
        self.input_text(self.LAST_NAME_INPUT, lastname)
        self.input_text(self.POSTAL_CODE_INPUT, postalcode)

    @allure.step("Продолжение оформления заказа")
    def continue_checkout(self) -> None:
        """Нажимает кнопку продолжения оформления заказа."""
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Получение итоговой стоимости")
    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа.

        Returns:
            str: текст с итоговой стоимостью
        """
        total_element = self.find_element(self.TOTAL_PRICE)
        return total_element.text
