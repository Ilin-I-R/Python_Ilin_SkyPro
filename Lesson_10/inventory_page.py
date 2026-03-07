from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class InventoryPage(BasePage):
    """Страница каталога товаров."""

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(@data-test, 'add-to-cart')]"
    )
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    @allure.step("Добавление первого товара в корзину")
    def add_first_item_to_cart(self) -> None:
        """Добавляет первый товар из списка в корзину."""
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons:
            add_buttons[0].click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину через иконку корзины."""
        self.click_element(self.SHOPPING_CART_LINK)

    @allure.step("Подсчёт товаров в каталоге")
    def get_inventory_items_count(self) -> int:
        """
        Считает количество товаров в каталоге.

        Returns:
            int: количество товаров
        """
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)
