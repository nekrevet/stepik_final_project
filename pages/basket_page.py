from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        'Empty basket message is not presented'

    def should_not_be_items_to_buy_now(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BY_NOW), \
        'Items to buy now are presented, but should not be'