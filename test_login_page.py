from pages.login_page import LoginPage

link = "https://www.imperiasumok.ru/auth/"

def test_guest_can_log_in(browser):
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.change_city()
    login_page.guest_can_login()
    login_page.user_can_logout()

def test_guest_can_go_to_register_page_from_auth_page(browser):
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.change_city()
    login_page.guest_can_go_to_register_page_from_login()
