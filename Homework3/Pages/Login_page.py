from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(object):

    def __init__(self, driver, base_url='https://anotepad.com/create_account'):
        self.base_url = base_url
        self.driver = driver

    def go_to_login_page(self):
        self.driver.find_element_by_link_text("Register/Login").click()

    def login(self, email, password):
        self.driver.find_element_by_css_selector("#loginEmail").send_keys(email)
        self.driver.find_element_by_css_selector("[placeholder='Enter Password']").send_keys(password)
        self.driver.find_element_by_xpath("//button[text()='Login']").click()

    def login_assertion(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
        finally:
            print("Login has not been done!")
            self.driver.quit()

    def submit_logout(self):
        self.driver.find_element_by_link_text("Logout").click()

    def logout_assertion(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register/Login")))
        finally:
            print("Logout has not been done!")
            self.driver.quit()