from pages.section_page import SectionPage

link = "https://www.imperiasumok.ru/catalog/"

def test_guest_can_add_product_to_cart(browser):
    section_page = SectionPage(browser, link)
    section_page.open()
    section_page.change_city()
    section_page.guest_can_add_goods_to_cart()

#def test_guest_can_use_filter(browser):
#    catalog_page = SectionPage(browser, link)
#    catalog_page.open()
#    catalog_page.change_city() -                  - Функция не готова

