from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import math
import time

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

class ProductPage(BasePage): 
    def add_product_to_cart(self):
        btn  = self.browser.find_element(*ProductPageLocators.ADD_TO_BASCET_BUTTON)
        btn.click()

        solve_quiz_and_get_code(self)

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_element(*ProductPageLocators.ALTER_PRDUCT_CONFIRM).text, f"Имя проукта не совпадает с добавленным"
