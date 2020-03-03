from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.locators import SectionPageLocators


class SectionPage(BasePage):

    def guest_can_add_goods_to_cart(self):
        first_product_add_to_cart = self.is_element_visible_and_click(SectionPageLocators.ADD_TO_CART_FIRST_PRODUCT)
        check_cart_value = self.browser.find_element(*BasePageLocators.CART_ICON)
        assert int(check_cart_value.text) == 1, 'Quantity in cart != 1'
        
    def guest_can_go_to_cart_page_from_section_page(self):
        check_cart_value = self.is_element_visible_and_click(BasePageLocators.CART_ICON)
        print(self.browser.current_url)
        assert self.browser.current_url == "https://www.imperiasumok.ru/personal/cart/", "Current url != /cart/ page"
    
   # def guest_can_use_filter(self):
        