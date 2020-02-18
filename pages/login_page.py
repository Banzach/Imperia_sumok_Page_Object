from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import BasePageLocators
import time

class LoginPage(BasePage):

    def guest_can_login(self):
        assert self.is_element_present(*LoginPageLocators.USER_LOGIN), 'Field for Login not present'
        assert self.is_element_present(*LoginPageLocators.USER_PASSWORD), 'Field for Paswword not present'
        input_login = self.browser.find_element(*LoginPageLocators.USER_LOGIN)
        input_login.click()
        input_login.send_keys('ImperTest25@gmail.com')
        input_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        input_password.click()
        input_password.send_keys('ImperTest25')
       
        log_in_button = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in_button.click()
        time.sleep(1)
        user_name_on_header = self.browser.find_element(*BasePageLocators.USER_NAME_ON_HEADER)
        assert user_name_on_header.text == "Auto_test Test", "Login name not match with Auto_test Test"
    
    def guest_can_go_to_register_page(self):
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
        assert self.browser.current_url == "https://www.imperiasumok.ru/reg/", "Current url not a /reg/ page"