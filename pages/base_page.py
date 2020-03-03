from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import BasePageLocators
from selenium.webdriver.common.by import By

class BasePage():

    # Создаем конструктор, методы которого будут вызываться при создании нового объекта
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)
  
    # Выбираем город, в котором возможно оформить заказ (к примеру г.Самара)
    def change_city(self):
        change_city = self.browser.find_element(*BasePageLocators.BUTTON_TO_CHANGE_CITY)
        change_city.click()
        change_city_to = self.browser.find_element(*BasePageLocators.BUTTON_TO_CHANGE_CITY_ON_THIS)
        change_city_to.click()
    
    # Переходим по ссылке
    def open(self):
        self.browser.get(self.url)  
        
    # Проверяем, виден ли элемент и кликаем по нему
    def is_element_visible_and_click(self, locator, time=20):
        try:
            is_element_visible = WebDriverWait(self.browser,time).until(
            EC.visibility_of_element_located(locator)).click()
        except(NoSuchElementException):
            return False
        return is_element_visible
        
    # Проверяем наличие элемента на странице  
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False, "Element is not present"
        return True
    
    # Ввод текст в какое-нибудь поле
    def input_message(self, how, what, message):
        input_field = self.browser.find_element(how, what)
        input_field.click()
        input_field.send_keys(message)
    
    # Скроллим страницу до нужного элемента
    def scroll_page_to(self, how, what):  
        target = self.browser.find_element(how, what)
        target.location_once_scrolled_into_view
    
    # Получаем значение аттрибута элемента 
    def get_element_attribute(self, how, what, attribute):
        return self.browser.find_element(how, what).get_attribute(attribute)

    # Пользователь может выйти из учетной записи на любой странице сайта
    def user_can_logout(self):
        logout_button = self.is_element_visible_and_click(BasePageLocators.LOGOUT_BUTTON)
    
    # Пользователь может перейти на страницу авторизации с любой страницы сайта
    def user_can_go_to_login_page(self):
        login_page_button = self.is_element_visible_and_click(BasePageLocators.LOGIN_PAGE)
        assert self.browser.current_url == "https://www.imperiasumok.ru/auth/", "Текущая страница != /auth/"
