from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    CURRENT_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    LOGIN_AREA = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_AREA = (By.CSS_SELECTOR, "#id_registration-email")

class ProductPageLocators:
    ADD_TO_BASCET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALTER_PRDUCT_CONFIRM = (By.CSS_SELECTOR, ".alertinner")