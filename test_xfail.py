from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
# для проверки бага поменяешь на:
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # уникальные селекторы только по обязательным полям блока first_class
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
    email.send_keys("test@test.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" in welcome_text

finally:
    time.sleep(5)
    browser.quit()
