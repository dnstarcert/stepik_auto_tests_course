from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)

    label= browser.find_element(By.CSS_SELECTOR, "input#answer")
    label.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    option2.click()

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

finally:
    time.sleep(20)
    browser.quit()





