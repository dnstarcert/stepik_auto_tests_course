from .locators import BasketLocators
from .base_page import BasePage
from time import sleep


class ProductPage(BasePage):
    def guest_should_be_add_product_to_basket(self):
        self.add_to_basket()

    def add_to_basket(self):
        button = self.browser.find_element(*BasketLocators.BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        product = self.browser.find_element(*BasketLocators.PRODUCT_NAME)
        return product.text

    def get_price(self):
        price = self.browser.find_element(*BasketLocators.PRICE)
        return price.text

    def get_basket_product_name(self):
        product = self.browser.find_element(*BasketLocators.BASKET_PRODUCT)
        return str(product.text).strip().rstrip()

    def get_basket_product_price(self):
        price = self.browser.find_element(*BasketLocators.BASKET_PRICE)
        return str(price.text).strip().rstrip()

    @staticmethod
    def product_must_match(how, what):
        assert how == what, "products do not match"

    @staticmethod
    def price_must_math(how, what):
        assert how == what, "price do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_not_dissapired(self):
        assert self.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE), \
            "Success message is dissapired, but should not be"