from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Smolensk")

        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        input2.send_keys("Smolensk")

        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input3.send_keys("Smolensk@smilensk.name")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         'Message should be "Congratulations! You have successfully registered!"')


    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Smolensk")

        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        input2.send_keys("Smolensk")

        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input3.send_keys("Smolensk@smilensk.name")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                        'Message should be "Congratulations! You have successfully registered!"')

if __name__ == "__main__":
    unittest.main()