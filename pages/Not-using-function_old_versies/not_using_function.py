
        
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




    #def find_element(self, locator, time=10):
    #    return WebDriverWait(self.browser,time).until(EC.element_to_be_clickable(locator))        # - Вместо time.sleep
        
    #element = WebDriverWait(driver, 20).until(
    #EC.presence_of_element_located((By.ID, "myElement")))    
    
    #def wait_until_element_clickable(self):
    #    return WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable((*CartPageLocators.DISCOUNT_CARD_FIELD)))