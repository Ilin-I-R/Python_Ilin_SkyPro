from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://uitestingplayground.com/classattr")
button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]"
    )
button.click()
sleep(2)
driver.quit()
