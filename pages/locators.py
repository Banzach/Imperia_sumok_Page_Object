from selenium.webdriver.common.by import By

class BasePageLocators():
    BODY = (By.TAG_NAME, "body")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".middle a #Layer_1")
    USER_NAME_ON_HEADER = (By.CSS_SELECTOR, ".middle [href = '/personal/'] span")
    SEARCH_BAR = (By.CSS_SELECTOR, ".middle [name='q']")
    GO_SEARCH_BUTTON = (By.CSS_SELECTOR, ".middle [type='submit']")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".result b")
    FAVORITE_ICON = (By.CSS_SELECTOR, ".hidden-header .elem-fav span")
    CART_ICON = (By.CSS_SELECTOR, ".hidden-header .count")
    BUTTON_TO_CHANGE_CITY = (By.CSS_SELECTOR, ".btn.btn-gray.hidden-xs")
    BUTTON_TO_CHANGE_CITY_ON_THIS = (By.PARTIAL_LINK_TEXT, "Челябинск")
    LOGIN_PAGE = (By.LINK_TEXT, "Вход")
    CHOOSE_SECTION_MAN_BAGS= (By.CSS_SELECTOR, ".nav-top.hidden-xs [href='/catalog/muzhskie-sumki/']")
    CHOOSE_SECTION_MAN = (By.LINK_TEXT, 'Мужчинам')

class LoginPageLocators():
    USER_LOGIN = (By.CSS_SELECTOR, "[name = 'USER_LOGIN']")
    USER_PASSWORD = (By.CSS_SELECTOR, "[name = 'USER_PASSWORD']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[name='Login']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".box-auth-reg a[href = '/reg/']")

class SectionPageLocators():
    FIRST_PRODUCT_CART = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .box-snippet-full.product_item")
    ADD_TO_FAVORITE_FIRST_PRODUCT = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .fa.fa-heart-o")
    ADD_TO_CART_FIRST_PRODUCT = (By.CSS_SELECTOR, ".row .col-xs-6.col-sm-6.col-md-4.col-lg-3:nth-child(1) .to_basket")
    SMART_FILTER = (By.CSS_SELECTOR, ".col-sm-4 .filter")

class CartPageLocators():
    FIRST_PICKUP_POINT = (By.CSS_SELECTOR, "[data-ng-if='delivery.SHOPS'] label:nth-child(1)")
    DISCOUNT_CARD_FIELD = (By.CSS_SELECTOR, "[name='barcode']")
    APPLY_DISCOUNT_CARD = (By.CSS_SELECTOR, "button.btn.btn-gray")
    NEXT_STEP = (By.CSS_SELECTOR, "a.btn.btn-blue.pull-right")
    CONTACT_DATA_NAME = (By.CSS_SELECTOR, "[name='name']")
