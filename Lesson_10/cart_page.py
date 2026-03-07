from selenium.webdriver.common.by import By
from base_page import BasePage
import allure


class CartPage(BasePage):
    """Страница корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.click_element(self.CHECKOUT_BUTTON)

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self) -> list[str]:
        """
        Получает названия всех товаров в корзине.

        Returns:
            list[str]: список названий товаров
        """
        item_elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in item_elements]

    @allure.step("Подсчёт количества товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Считает количество товаров в корзине.

        Returns:
            int: количество товаров (минус один служебный элемент)
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) - 1
