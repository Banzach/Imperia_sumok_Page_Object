from pages.section_page import SectionPage
from pages.locators import CartPageLocators
from pages.cart_page import CartPage

link = "https://www.imperiasumok.ru/catalog/muzhskie-sumki/"

def test_guest_can_create_order(browser):

    section_page = SectionPage(browser, link)
    cart_page = CartPage(browser, link)
    
    section_page.open()
    section_page.change_city()
    section_page.guest_can_add_goods_to_cart_and_favorite()
    section_page.guest_can_go_to_cart_page_from_section_page()
    
    # Переходим на страницу корзины
    cart_page.guest_can_choose_pickup_point()
    cart_page.guest_can_input_discount_card()
    cart_page.guest_can_go_to_next_step_create_order()
    cart_page.guest_can_input_contact_data()