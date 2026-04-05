from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_success_message(self, expected_name):
        message_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert message_name == expected_name, \
            f"Product name in message is '{message_name}', expected '{expected_name}'"

    def should_be_correct_basket_total(self, expected_price):
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE
        ).text
        assert basket_total == expected_price, \
            f"Basket total '{basket_total}' is not equal to product price '{expected_price}'"

    # отрицательные проверки

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should"