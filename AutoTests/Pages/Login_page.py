import allure
import allure_pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(object):

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Go to the Register/Login page")
    def go_to_login_page(self):
        self.browser.find_element_by_link_text("Register/Login").click()

    @allure.step("Login into the system")
    def login(self, email, password):
        self.browser.find_element_by_css_selector("#loginEmail").send_keys(email)
        self.browser.find_element_by_css_selector("[placeholder='Enter Password']").send_keys(password)
        self.browser.find_element_by_xpath("//button[text()='Login']").click()

    @allure.step("Check that login was successful")
    def login_assertion(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        except NoSuchElementException:
            print("Login has not been done!")
            return False

    @allure.step("Logout from the system")
    def submit_logout(self):
        self.browser.find_element_by_link_text("Logout").click()

    @allure.step("Check that logout was successful")
    def logout_assertion(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register/Login")))
        except NoSuchElementException:
            print("Logout has not been done!")
            return False