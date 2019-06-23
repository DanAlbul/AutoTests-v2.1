import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from Pages.Login_page import Login
from Pages.Home_page import HomePage

link = "https://anotepad.com/create_account"
email = "kair317@gmail.com"
password = "1234567"
note = "FNote 3"

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()

class TestPublicOrPrivateSave(object):

    def test_public_or_private_save(self, browser):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
        login.login_assertion()

        home_page = HomePage(browser)

        #public
        home_page.select_note(note)

        home_page.public_or_private_setting()

        home_page.public_checkbox()

        home_page.public_selected_assert()

        #private
        home_page.select_note(note)

        home_page.public_or_private_setting()

        home_page.private_checkbox()

        home_page.private_selected_assert()
