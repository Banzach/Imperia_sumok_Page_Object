from pages.main_page import MainPage

link = "https://www.imperiasumok.ru/"

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.change_city()
    main_page.user_can_go_to_login_page()
    main_page.should_be_login_page()
    
def test_guest_use_search(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.change_city()
    main_page.guest_should_can_use_search()

def test_guest_can_go_to_sections_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.change_city()
    main_page.guest_should_can_go_to_sections_page()