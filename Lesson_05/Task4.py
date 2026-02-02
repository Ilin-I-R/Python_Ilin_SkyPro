from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.NAME, "username").send_keys("tomsmith")
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
sleep(1)
driver.find_element(By.TAG_NAME, "button").click()
input_field = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
sleep(1)
driver.quit()
