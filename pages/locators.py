from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".middle a #Layer_1")
    USER_NAME_ON_HEADER = (By.CSS_SELECTOR, ".middle [href = '/personal/'] span")
    
class MainPageLocators():
    BUTTON_TO_CHANGE_CITY = (By.CSS_SELECTOR, ".btn.btn-gray.hidden-xs")
    BUTTON_TO_CHANGE_CITY_ON_THIS = (By.PARTIAL_LINK_TEXT, "Самара")
    LOGIN_PAGE = (By.LINK_TEXT, "Вход")
    
class LoginPageLocators():
    USER_LOGIN = (By.CSS_SELECTOR, "[name = 'USER_LOGIN']")
    USER_PASSWORD = (By.CSS_SELECTOR, "[name = 'USER_PASSWORD']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[name='Login']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".box-auth-reg a[href = '/reg/']")
    
    