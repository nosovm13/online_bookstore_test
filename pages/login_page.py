from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/accounts/login" in self.browser.current_url, f"Ожидали URL логина, а получен {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.if_element_present(*LoginPageLocators.LOGIN_AREA), "Поле ввода логина не обнаружено"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.if_element_present(*LoginPageLocators.REGISTER_AREA), "Поле регистрации не обнаружено"