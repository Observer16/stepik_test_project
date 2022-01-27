from .pages.product_page import ProductPage
import pytest

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_list = [base_link + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offerN has bug, will mark it as xfail
link_list_with_xfail = [pytest.param(link, marks=pytest.mark.xfail) if link[-1] == "N" else link for link in link_list]

@pytest.mark.parametrize('link', link_list_with_xfail)
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()           # Очистить Cookies перед тестом
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем 
    page.add_to_basket()        # выполняем метод страницы — переходим на страницу продукт
    page.should_be_product_name ()     # проверяем соответствие продукта