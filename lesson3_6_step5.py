import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', [
                                   "https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"
                                   ])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, links):
        link = f"{links}"
        browser.get(link)
        browser.implicitly_wait(5)
        login = browser.find_element(By.ID,"ember33")
        login.click()
        enter_login = browser.find_element(By.ID, "id_login_email")
        enter_login.send_keys('gendalf1984@gmail.com')
        enter_passwd = browser.find_element(By.ID, "id_login_password")
        enter_passwd.send_keys('Lt50jVOb8tZvypXX')
        log_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        log_button.click()
        browser.find_element(By.CSS_SELECTOR, "button.navbar__profile-toggler")
        text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        try:
            answer = math.log(int(time.time()))
            text_area.send_keys(answer)
            btn = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
            btn.click()
        except:
            pass
        ans = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        assert "Correct!" in ans.text

