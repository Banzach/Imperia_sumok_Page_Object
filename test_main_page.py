from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "https://test.imperiasumok.ru/"
    page = MainPage(browser, link)
    page.open()
    page.change_city()
    page.user_can_go_to_login_page()
    page.is_it_login_page()