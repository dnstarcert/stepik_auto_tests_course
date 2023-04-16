from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class BasketLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_PRODUCT = (By.XPATH, "//*[@id=\"messages\"]/div[1]/div/strong")
    BASKET_PRICE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")



