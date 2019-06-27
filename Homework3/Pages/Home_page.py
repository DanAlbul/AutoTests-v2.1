import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(object):
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Go to the Home page")
    def go_to_home_page(self):
        self.browser.find_element_by_link_text("Home").click()

    @allure.step("Select a note")
    def select_note(self, note):
        self.browser.find_element_by_link_text(note).click()

    @allure.step("Open Public/Private note settings")
    def public_or_private_setting(self):
        self.browser.find_element_by_css_selector(".caret").click()

    @allure.step("Choose 'Public' flag")
    def public_checkbox(self):
        self.browser.find_element_by_id("accesspublic").click()
        self.browser.find_element_by_css_selector(".btn.btn-default").click()

    @allure.step("Choose 'Private' flag")
    def private_checkbox(self):
        self.browser.find_element_by_id("accessprivate").click()
        self.browser.find_element_by_css_selector(".btn.btn-default").click()

    @allure.step("Check that note is now 'Public'")
    def public_selected_assert(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//strong[contains(text(), 'Public Note')]")))
           # self.browser.find_element_by_id("saveNoteMessage")
        except NoSuchElementException:
            print("Note private settings is not changed! Note is still public.")
            return False

    @allure.step("Check that note is now 'Private'")
    def private_selected_assert(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(
                (By.XPATH, "//strong[contains(text(), 'Private Note')]")))
           # self.browser.find_element_by_id("saveNoteMessage")
        except NoSuchElementException:
            print("Note private settings is not changed! Note is still private.")
            return False