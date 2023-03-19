from selenium.webdriver.common.by import By
from time import sleep
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    button_exist = None
    if browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"):
        button_exist = "True"
    else:
        button_exist = "False"
    sleep(5)
    assert "True" in button_exist
