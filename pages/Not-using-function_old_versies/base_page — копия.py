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

    #def find_element(self, locator, time=10):
    #    return WebDriverWait(self.browser,time).until(EC.element_to_be_clickable(locator))        # - Вместо time.sleep
        
    def is_element_clickable(self, locator, time=10):
        return WebDriverWait(self.browser,time).until(EC.element_to_be_clickable(locator))        # - Вместо time.sleep
        
    def open(self):
        self.browser.get(self.url)
        
    def change_city(self):
        change_city = self.is_element_clickable(BasePageLocators.BUTTON_TO_CHANGE_CITY)
        change_city.click()
        change_city_on = self.is_element_clickable(BasePageLocators.BUTTON_TO_CHANGE_CITY_ON_THIS)
        #change_city_on= self.browser.find_element(*BasePageLocators.BUTTON_TO_CHANGE_CITY_ON_THIS)
        change_city_on.click()
        
    def user_can_go_to_login_page(self):
        login_page_button = self.is_element_clickable(BasePageLocators.LOGIN_PAGE)
        login_page_button.click()
    
    def should_be_login_page(self):
        assert self.browser.current_url == "https://www.imperiasumok.ru/auth/", "Not the auth page"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False, "Element is not present" # не уверен, что комментарий будет отображаться - проверить.                        !!!!
        return True
    
    def user_can_logout(self):
        logout_button = self.browser.find_element(*BasePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        time.sleep(1)
        
    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 550);") # "Импортируем" код из JS для скролла страницы
        time.sleep(0.5)
        



        
    #element = WebDriverWait(driver, 20).until(
    #EC.presence_of_element_located((By.ID, "myElement")))    
    #def wait_until_element_clickable(self):
    #    return WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable((*CartPageLocators.DISCOUNT_CARD_FIELD)))
