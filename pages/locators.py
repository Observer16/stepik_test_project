from selenium.webdriver.common.by import By

'''
Каждый класс будет соответствует каждому классу PageObject
'''

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")