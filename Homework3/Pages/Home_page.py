from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class HomePage(object):
    def __init__(self, driver, base_url='https://anotepad.com/'):
        self.base_url = base_url
        self.driver = driver

    def go_to_home_page(self):
        self.driver.find_element_by_link_text("Home").click()

    def select_note(self, title):
        self.driver.find_element_by_link_text(title).click()

    def public_or_private_setting(self):
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'Public')]")
        finally:
            self.driver.find_element_by_xpath("//strong[contains(text(),'Private')]")

    def public_checkbox(self):
        select = Select.self.driver.find_element_by_id("accesspublic")
        select.select_by_visible_text("Public Note")
        self.driver.find_element_by_css_selector(".btn.btn-default").click()

    def private_checkbox(self):
        select = Select.self.driver.find_element_by_id("accessprivate")
        select.select_by_visible_text("Private Note")
        self.driver.find_element_by_css_selector(".btn.btn-default").click()

    def public_selected_assert(self):
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'Public')]")
        finally:
            print("Note is public now!")
            self.driver.quit()

    def private_selected_assert(self):
        try:
            self.driver.find_element_by_xpath("//strong[contains(text(),'Private')]")
        finally:
            print("Note is private now!")
            self.driver.quit()