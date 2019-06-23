from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(object):
    def __init__(self, browser):
        self.browser = browser

    def go_to_home_page(self):
        self.browser.find_element_by_link_text("Home").click()

    def select_note(self, note):
        self.browser.find_element_by_link_text(note).click()

    def public_or_private_setting(self):
        self.browser.find_element_by_css_selector(".caret").click()

    def public_checkbox(self):
        self.browser.find_element_by_id("accesspublic").click()
        self.browser.find_element_by_css_selector(".btn.btn-default").click()

    def private_checkbox(self):
        self.browser.find_element_by_id("accessprivate").click()
        self.browser.find_element_by_css_selector(".btn.btn-default").click()

    def public_selected_assert(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//strong[contains(text(), 'Public Note')]")))
           # self.browser.find_element_by_id("saveNoteMessage")
        except NoSuchElementException:
            print("Note private settings is not changed! Note is still public.")
            return False

    def private_selected_assert(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//strong[contains(text(), 'Private Note')]")))
           # self.browser.find_element_by_id("saveNoteMessage")
        except NoSuchElementException:
            print("Note private settings is not changed! Note is still private.")
            return False