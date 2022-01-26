from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.ID)
        assert self.is_element_present(*LoginPageLocators.ID), "Login link is not presented"
        '''Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, 
        и этот кортеж нужно распаковать.'''

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True