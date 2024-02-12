from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")


    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)").send_keys("Dima")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)").send_keys('Fomin')
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)").send_keys('email@ya.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла