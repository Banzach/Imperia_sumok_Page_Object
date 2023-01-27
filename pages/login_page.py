from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import BasePageLocators

class LoginPage(BasePage):

    def guest_can_login(self):
        assert self.is_element_present(*LoginPageLocators.USER_LOGIN), 'Field for Login not present'
        assert self.is_element_present(*LoginPageLocators.USER_PASSWORD), 'Field for Paswword not present'
        login_field = self.input_message(*LoginPageLocators.USER_LOGIN, 'IMP')
        password_field = self.input_message(*LoginPageLocators.USER_PASSWORD, 'IMP')
   
        self.is_element_visible_and_click(LoginPageLocators.LOG_IN_BUTTON)
        user_name_on_header = self.browser.find_element(*BasePageLocators.USER_NAME_ON_HEADER)
        assert user_name_on_header.text == "Auto_test Test", "Login name not match with Auto_test Test"
    
    def guest_can_go_to_register_page_from_login(self):
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
        assert self.browser.current_url == "https://www.imperiasumok.ru/reg/", "Current url not a /reg/ page"
