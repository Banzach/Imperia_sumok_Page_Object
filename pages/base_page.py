from pages.locators import MainPageLocators
from pages.locators import BasePageLocators
from pages.locators import LoginPageLocators 
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url):  #__init создает конструктор метод, вызываемый при создании обхекта
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
        
    def change_city(self):
        change_city = self.browser.find_element(*MainPageLocators.BUTTON_TO_CHANGE_CITY)
        change_city.click()
        time.sleep(1)
        change_city_on= self.browser.find_element(*MainPageLocators.BUTTON_TO_CHANGE_CITY_ON_THIS)
        change_city_on.click()
        
    def user_can_go_to_login_page(self):
        login_page_button = self.browser.find_element(*MainPageLocators.LOGIN_PAGE)
        login_page_button.click()
    
    def is_it_login_page(self):
        assert self.browser.current_url == "https://www.imperiasumok.ru/auth/", "Not the auth page"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False, "Нет такого элемента" # не уверен, что причина работает правильно
        return True
    
    def user_can_logout(self):
        logout_button = self.browser.find_element(*BasePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        time.sleep(1)
    
    
    #base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

#locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

#main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

#И вот тут ступор. Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.
        
    
