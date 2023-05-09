from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket button is not presented'

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_message(self):
        message = self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        assert message, 'Added to basket message is not presented'

    def product_name_matches(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert name == name_in_message, 'Product name does not match'

    def should_be_basket_cost_message(self):
        cost_message = self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE)
        assert cost_message, 'Basket cost message is not presented'

    def basket_cost_matches_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_price == basket_cost, 'Basket cost does not match product price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Success message is presented, but should not be'

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        'Success message is not disappeared'