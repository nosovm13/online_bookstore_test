from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    CURRENT_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    LOGIN_AREA = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_AREA = (By.CSS_SELECTOR, "#id_registration-email")

