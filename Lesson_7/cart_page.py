from selenium.webdriver.common.by import By
from base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def get_cart_items(self):
        item_elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in item_elements]

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) - 1
