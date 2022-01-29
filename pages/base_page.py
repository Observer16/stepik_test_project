from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():

    def open(self):
        '''метод открывает нужную страницу, используя метод get()'''
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        '''команда для неявного ожидания со значением по умолчанию в 10'''
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        '''в классе реализуем метод is_element_present, в котором будем перехватывать исключение. 
        В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что 
        искать (строку-селектор). 
        Чтобы перехватывать исключение, нужна конструкция try/except'''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        '''абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени'''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        '''Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе 
        с функцией until_not, в зависимости от того, какой результат мы ожидаем
        '''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):          # Используйте этот метод в тесте для получения проверочного кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        try:
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
            link.click()
        except NoSuchElementException:
            print("No Login link page")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            
