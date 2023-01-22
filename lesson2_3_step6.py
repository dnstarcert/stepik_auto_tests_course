from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

browser = webdriver.Chrome()


def calc(xx):
    return str(math.log(abs(12 * math.sin(int(xx)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    label = browser.find_element(By.CSS_SELECTOR, "input#answer")
    label.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:
    sleep(10)
    browser.quit()