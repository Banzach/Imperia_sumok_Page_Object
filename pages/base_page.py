from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import BasePageLocators
from pages.locators import CartPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class BasePage():

    def __init__(self, browser, url):  #__init__ создает конструктор метод, вызываемый при создании объекта
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)
        
    def open(self):
        self.browser.get(self.url)
        
    def change_city(self):
        change_city = self.is_element_visible_and_click(BasePageLocators.BUTTON_TO_CHANGE_CITY)
        change_city_on = self.is_element_visible_and_click(BasePageLocators.BUTTON_TO_CHANGE_CITY_ON_THIS)
        
    def user_can_go_to_login_page(self):
        login_page_button = self.is_element_clickable(BasePageLocators.LOGIN_PAGE)
        login_page_button.click()
    
    def should_be_login_page(self):
        assert self.browser.current_url == "https://www.imperiasumok.ru/auth/", "Not the auth page"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False, "Element is not present"
        return True
    
    def user_can_logout(self):
        logout_button = self.is_element_visible_and_click(BasePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        time.sleep(1)
        
    def input_message(self, how, what, message):
        input_field = self.browser.find_element(how, what)
        input_field.click()
        input_field.send_keys(message)
    
    def is_element_visible_and_click(self, locator, time=20):
        return WebDriverWait(self.browser,time).until(EC.visibility_of_element_located(locator)).click()        # - Вместо time.sleep
    
    def scroll_page_to(self, how, what):  
        target = self.browser.find_element(how, what)
        target.location_once_scrolled_into_view


