from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.locators import SectionPageLocators
from pages.locators import CartPageLocators
import time

class SectionPage(BasePage):

    def guest_can_add_goods_to_cart_and_favorite(self):
        first_product_add_to_favorite = self.browser.find_element(*SectionPageLocators.ADD_TO_FAVORITE_FIRST_PRODUCT)
        first_product_add_to_favorite.click()
        first_product_add_to_cart = self.browser.find_element(*SectionPageLocators.ADD_TO_CART_FIRST_PRODUCT)
        first_product_add_to_cart.click()
        check_favorite_value = self.browser.find_element(*BasePageLocators.FAVORITE_ICON)
        check_cart_value = self.browser.find_element(*BasePageLocators.CART_ICON)
        time.sleep(1)
        assert int(check_favorite_value.text) == 1, 'Quantity in favorite is not = 1'
        assert int(check_cart_value.text) == 1, 'Quantity in cart is not = 1'
    
    def guest_can_go_to_cart_page_from_section_page(self):
        check_cart_value = self.browser.find_element(*BasePageLocators.CART_ICON)
        check_cart_value.click()
        time.sleep(0.5)
        print(self.browser.current_url)
        assert self.browser.current_url == "https://www.imperiasumok.ru/personal/cart/", "Current url not a /cart/ page"
    
    def guest_can_choose_pickup_point(self):
        first_pickup_point = self.browser.find_element(*CartPageLocators.FIRST_PICKUP_POINT)
        first_pickup_point.click()
        
    def guest_can_input_discount_card(self):
        input_discount_card = self.browser.find_element(*CartPageLocators.DISCOUNT_CARD_FIELD)
        input_discount_card.click()
        input_discount_card.send_keys('2670000000072')
        apply_discount_card = self.browser.find_element(*CartPageLocators.APPLY_DISCOUNT_CARD)
        apply_discount_card.click()
        
    def guest_can_go_to_next_step_create_order(self):
        go_to_next_step = self.browser.find_element(*CartPageLocators.NEXT_STEP)
        go_to_next_step.click()



#    def __init__(self, *args, **kwargs):                      --------- ЗАГЛУШКА
#        super(SectionPage, self).__init__(*args, **kwargs)

# **kwargs и *args позволяют использовать в функции неопределенное количество именованных и неименованных аргументов соответственно.
