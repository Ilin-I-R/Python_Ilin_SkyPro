from selenium.webdriver.common.by import By
from base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(@data-test, 'add-to-cart')]"
    )
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def add_first_item_to_cart(self):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons:
            add_buttons[0].click()

    def go_to_cart(self):
        self.click_element(self.SHOPPING_CART_LINK)

    def get_inventory_items_count(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)
