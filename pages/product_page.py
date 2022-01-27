from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Button is not presented"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()      # Решение задачи в alert
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name doesn't match"

    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name == product_basket, "Name is not same"