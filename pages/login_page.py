from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from pages.locators import BasePageLocators
import time

class LoginPage(BasePage):

    def guest_can_login(self):
        # Check fields for auth
        assert self.is_element_present(*LoginPageLocators.USER_LOGIN), 'Field for Login not present'
        assert self.is_element_present(*LoginPageLocators.USER_PASSWORD), 'Field for Paswword not present'
        # Input user login&pass
        input_login = self.browser.find_element(*LoginPageLocators.USER_LOGIN)
        input_login.click()
        input_login.send_keys('yurchserg1@gmail.com')
        input_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        input_password.click()
        input_password.send_keys('9umywepv')
       
        log_in_button = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in_button.click()
        time.sleep(1)
        user_name_on_header = self.browser.find_element(*BasePageLocators.USER_NAME_ON_HEADER)
        assert user_name_on_header.text == "Сергей Юрченко", "Login name not match with Сергей Юрченко"
    
    def guest_can_go_to_register_page(self):
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
        assert self.browser.current_url == "https://test.imperiasumok.ru/reg/", "Current url not a /reg/ page"

    
    
    #base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

#locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

#main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

#И вот тут ступор. Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.
        
    
