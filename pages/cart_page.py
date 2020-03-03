from pages.locators import BasePageLocators
from pages.locators import CartPageLocators
from pages.base_page import BasePage

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
        self.input_message(*CartPageLocators.CONTACT_DATA_NAME, "AutoTest")
        self.input_message(*CartPageLocators.CONTACT_DATA_LASTNAME, "AutoTest")
        self.input_message(*CartPageLocators.CONTACT_DATA_EMAIL, "ImperTest25@gmail.com")
        self.input_message(*CartPageLocators.CONTACT_DATA_MESSAGE, "СъешьЕщеЭтихМягкихФранцузскихБулок,ДаВыпейЧаю")
       # Проверяем, установлена ли максимальная длина комментария
        commentary_length = self.get_element_attribute(*CartPageLocators.CONTACT_DATA_MESSAGE,"maxlength")
        assert int(commentary_length) == 200, "Maxlength of commentary != 200"
        