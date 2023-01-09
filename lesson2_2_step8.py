from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'txt.txt')           # добавляем к этому пути имя файла
browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Smolensk")

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Smolensk")

    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("Smolensk@smilensk.name")

    element = browser.find_element(By.CSS_SELECTOR, 'input#file')
    element.send_keys(file_path)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:
    time.sleep(20)
    browser.quit()
