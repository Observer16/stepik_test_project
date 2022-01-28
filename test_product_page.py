from .pages.product_page import ProductPage
import pytest


base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_list = [base_link + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offerN has bug, will mark it as xfail
link_list_with_xfail = [pytest.param(link, marks=pytest.mark.xfail) if link[-1] == "N" else link for link in link_list]

@pytest.mark.skip
@pytest.mark.parametrize('link', link_list_with_xfail)
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()           # Очистить Cookies перед тестом
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем 
    page.add_to_basket()        # выполняем метод страницы — переходим на страницу продукт
    page.should_be_product_name ()     # проверяем соответствие продукта


@pytest.mark.skip
@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()           # Очистить Cookies перед тестом
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()                # выполняем метод страницы — переходим на страницу продукт и добавляем товар в карзинц
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    browser.delete_all_cookies()           # Очистить Cookies перед тестом
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.xfail(reason="not disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()           # Очистить Cookies перед тестом
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    page.add_to_basket()                # выполняем метод страницы — переходим на страницу продукт и добавляем товар в карзинц
    page.element_disappears_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()