from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
import time

class MainPage(BasePage):
    
    def test_guest_can_use_search(self):
        search_bar = self.browser.find_element(*BasePageLocators.SEARCH_BAR)
        search_bar.click()
        search_bar.send_keys('сумка')
        go_search_button = self.browser.find_element(*BasePageLocators.GO_SEARCH_BUTTON)
        go_search_button.click()
        is_search_result = self.is_element_present(*BasePageLocators.SEARCH_RESULTS)
        search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULTS)
        assert int(search_result.text) >= 300, "Few results for search on 'Сумка'" 
    
    def should_can_go_to_sections_page(self):
        choose_section_man = self.browser.find_element(*MainPageLocators.CHOOSE_SECTION_MAN)
        choose_section_man.click()
        time.sleep(0.5)
        choose_section_man_bags = self.browser.find_element(*MainPageLocators.CHOOSE_SECTION_MAN_BAGS)
        choose_section_man_bags.click()
        assert self.browser.current_url == "https://www.imperiasumok.ru/catalog/muzhskie-sumki/", "Not /muzhskie-sumki/ page"
        
    
    
    
    
    
    
    
    
#    def __init__(self, *args, **kwargs):                      --------- ЗАГЛУШКА
#        super(MainPage, self).__init__(*args, **kwargs)
    
    
    
    
    #base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

#locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

#main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

#И вот тут ступор. Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.
        
    
