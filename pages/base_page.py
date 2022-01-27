from os import link
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class BasePage(object):

    def __init__(self, browser, url):
        """Конструктор класса.
        :параметр browser:
        :параметр url:
        """
        self.browser = browser
        self.url = url

    def open(self):
        '''метод открывает нужную страницу, используя метод get()'''
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        '''команда для неявного ожидания со значением по умолчанию в 10'''
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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

