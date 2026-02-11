from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()
text = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
).text
print(text)
driver.quit()
