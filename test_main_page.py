import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_go_to_login_page(browser):
    link = " http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    #login_page = LoginPage(browser, browser.current_url) # позволяет явно инициализировать новую страницу правильным образом

def test_guest_should_see_correct_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_should_see_correct_login_page_after_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    mainPage = MainPage(browser, link)
    mainPage.open()
    loginPage = mainPage.go_to_login_page()
    loginPage.should_be_login_page()