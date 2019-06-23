from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Settings(object):
    def __init__(self, browser):
        self.browser = browser

    def go_to_settings_page(self):
        self.browser.find_element_by_link_text("Settings").click()

    def change_email(self, email):
        self.browser.find_element_by_css_selector("#email").send_keys(email)
        self.browser.find_element_by_css_selector("[value='Update Email']").click()

    def email_update_assertion(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//p[text()='Email updated successfully']")))
        except NoSuchElementException:
            print("Email is not changed!")
            return False

    def change_password(self, password):
        self.browser.find_element_by_css_selector("#password").send_keys(password)
        self.browser.find_element_by_css_selector("#password_confirm").send_keys(password)
        self.browser.find_element_by_css_selector("[value='Update Password']").click()

    def password_update_assertion(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//p[text()='Password successfully reset']")))
        except NoSuchElementException:
            print("Password is not changed!")
            return False

    def update_any_settings(self):
        self.browser.find_element_by_css_selector("[value='Update Settings']").click()