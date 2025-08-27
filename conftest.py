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

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Select the browser language")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")        #беру user_language из language

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()