from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
y_element = browser.find_element(By.CSS_SELECTOR, "#num2")

res = str(int(x_element.text) + int(y_element.text))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(res)

button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
button1.click()

time.sleep(20)

browser.quit()