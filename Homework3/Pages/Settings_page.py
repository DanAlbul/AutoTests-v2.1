from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Settings(object):

    def __init__(self, driver, base_url='https://anotepad.com/'):
        self.base_url = base_url
        self.driver = driver

    def go_to_settings_page(self):
        self.driver.find_element_by_link_text("Settings").click()

    def change_email(self, email):
        self.driver.find_element_by_css_selector("#email").send_keys(email)
        self.driver.find_element_by_css_selector("[value='Update Email']").click()

    def email_update_assertion(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//p[text()='Email updated successfully']")))
        finally:
            print("Email is not changed!")
            self.driver.quit()

    def change_password(self, password):
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_css_selector("#password_confirm").send_keys(password)
        self.driver.find_element_by_css_selector("[value='Update Password']").click()

    def password_update_assertion(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//p[text()='Password successfully reset']")))
        finally:
            print("Password is not changed!")
            self.driver.quit()

    def update_any_settings(self):
        self.driver.find_element_by_css_selector("[value='Update Settings']").click()