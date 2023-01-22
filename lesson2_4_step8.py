from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
label = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

button = browser.find_element(By.ID, "book")
button.click()

def calc(xx):
    return str(math.log(abs(12 * math.sin(int(xx)))))


x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
x = x_element.text
y = calc(x)

label = browser.find_element(By.CSS_SELECTOR, "input#answer")
label.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR, "button#solve")
button1.click()

sleep(30)
browser.quit()
#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text