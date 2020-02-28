from pages.locators import BasePageLocators
from pages.locators import CartPageLocators
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    
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
#        super(MainPage, self).__init__(*args, **kwargs)
