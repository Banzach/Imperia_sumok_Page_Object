from pages.locators import BasePageLocators
from pages.locators import CartPageLocators
from pages.base_page import BasePage
import time

class CartPage(BasePage):
  
    def guest_can_choose_pickup_point(self):
        self.scroll_page_to(*CartPageLocators.FIRST_PICKUP_POINT)
        self.is_element_visible_and_click(CartPageLocators.FIRST_PICKUP_POINT)
        
    def guest_can_input_discount_card(self):
        self.scroll_page_to(*CartPageLocators.DISCOUNT_CARD_FIELD)
        self.input_message(*CartPageLocators.DISCOUNT_CARD_FIELD, "2670000000072")
        self.is_element_visible_and_click(CartPageLocators.APPLY_DISCOUNT_CARD)
        
    def guest_can_go_to_next_step_create_order(self):
        go_to_next_step = self.browser.find_element(*CartPageLocators.NEXT_STEP)
        go_to_next_step.click()
        
    def guest_can_input_contact_data(self):
        self.input_message(*CartPageLocators.CONTACT_DATA_NAME, "Serega")