from selenium.webdriver.common.by import By

'''
Каждый класс будет соответствует каждому классу PageObject
'''

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")