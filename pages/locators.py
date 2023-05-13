from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span.btn-group>a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)>.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1)>.alertinner>strong')
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(3)>.alertinner>p')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    BASKET_COST = (By.CSS_SELECTOR, '.alert:nth-child(3)>.alertinner>p>strong')

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '.content p')
    ITEMS_TO_BY_NOW = (By.CSS_SELECTOR, '.h3:nth-child(1)')