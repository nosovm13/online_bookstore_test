from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 
        return LoginPage(browser=self.browser, url=self.browser.current_url)        #неявная инициализация страницы после перехода на неё

    def should_be_login_link(self):
        assert self.if_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка не обнаружена"
