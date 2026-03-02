from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.spinner = (By.ID, "spinner")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds):
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button_7(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_7)
        )
        button.click()

    def click_button_8(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_8)
        )
        button.click()

    def click_plus(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button.click()

    def click_equals(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button.click()

    def get_result(self):
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.result_screen)
        )
        return result_element.text

    def wait_for_calculation_complete(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.spinner)
        )
