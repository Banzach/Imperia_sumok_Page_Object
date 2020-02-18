from pages.base_page import BasePage
from pages.locators import BasePageLocators
import time

class MainPage(BasePage):
    
    def guest_should_can_use_search(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_BAR), 'Search bar not present'
        search_bar = self.browser.find_element(*BasePageLocators.SEARCH_BAR)
        search_bar.click()
        search_bar.send_keys('сумка')
        go_search_button = self.browser.find_element(*BasePageLocators.GO_SEARCH_BUTTON)
        go_search_button.click()
        is_search_result = self.is_element_present(*BasePageLocators.SEARCH_RESULTS)
        search_result = self.browser.find_element(*BasePageLocators.SEARCH_RESULTS)
        assert int(search_result.text) >= 300, "Few results for search on 'Сумка'" 
    
    def guest_should_can_go_to_sections_page(self):
        choose_section_man = self.browser.find_element(*BasePageLocators.CHOOSE_SECTION_MAN)
        choose_section_man.click()
        time.sleep(0.5)
        choose_section_man_bags = self.browser.find_element(*BasePageLocators.CHOOSE_SECTION_MAN_BAGS)
        choose_section_man_bags.click()
        print(f"Current url = {self.browser.current_url}")
        assert self.browser.current_url == "https://www.imperiasumok.ru/catalog/muzhskie-sumki/", "Not /muzhskie-sumki/ page"
    
    
    
    
    
    
#    def __init__(self, *args, **kwargs):                      --------- ЗАГЛУШКА
#        super(MainPage, self).__init__(*args, **kwargs)
