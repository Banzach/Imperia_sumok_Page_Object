from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.locators import SectionPageLocators
from pages.locators import CartPageLocators

class SectionPage(BasePage):

    def guest_can_add_goods_to_cart_and_favorite(self):
        first_product_add_to_cart = self.is_element_visible_and_click(SectionPageLocators.ADD_TO_CART_FIRST_PRODUCT)
        check_cart_value = self.browser.find_element(*BasePageLocators.CART_ICON)
        assert int(check_cart_value.text) == 1, 'Quantity in cart is not = 1'

    
    def guest_can_go_to_cart_page_from_section_page(self):
        check_cart_value = self.is_element_visible_and_click(BasePageLocators.CART_ICON)
        print(self.browser.current_url)
        assert self.browser.current_url == "https://www.imperiasumok.ru/personal/cart/", "Current url not a /cart/ page"
        
#    def guest_can_choose_pickup_point(self):
#        scroll_page_to(CartPageLocators.FIRST_PICKUP_POINT)
#        first_pickup_point = self.is_element_visible_and_click(CartPageLocators.FIRST_PICKUP_POINT)
#        #element = wait_until_element_clickable(self, *CartPageLocators.DISCOUNT_CARD_FIELD) # - исполняется, но не работает

#    def guest_can_input_discount_card(self):
#        scroll_page_to(CartPageLocators.DISCOUNT_CARD_FIELD)
#        input_message(CartPageLocators.DISCOUNT_CARD_FIELD, "2670000000072")
#       apply_discount_card = self.is_element_visible_and_click(CartPageLocators.APPLY_DISCOUNT_CARD)


        # ЗАГЛУШКА
        #def __init__(self, *args, **kwargs):
        #super(SectionPage, self).__init__(*args, **kwargs)
        # **kwargs и *args позволяют использовать в функции неопределенное количество именованных и неименованных аргументов соответственно.
        
        #Делаем скриншот страницы
        #body = self.is_element_visible_and_click(BasePageLocators.BODY)
        #body.screenshot("screenshot_full.png")



