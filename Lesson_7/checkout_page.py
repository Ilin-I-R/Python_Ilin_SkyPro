from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, firstname, lastname, postalcode):
        self.input_text(self.FIRST_NAME_INPUT, firstname)
        self.input_text(self.LAST_NAME_INPUT, lastname)
        self.input_text(self.POSTAL_CODE_INPUT, postalcode)

    def continue_checkout(self):
        self.click_element(self.CONTINUE_BUTTON)

    def get_total_price(self):
        total_element = self.find_element(self.TOTAL_PRICE)
        return total_element.text
