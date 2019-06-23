import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from Pages.Login_page import Login
from Pages.Home_page import HomePage
from Pages.Settings_page import Settings

link = "https://anotepad.com/create_account"
email = "kair317@gmail.com"
old_password = "1234567"
new_password = "7777611"

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()

class TestChangePassword(object):

    def test_change_password(self, browser):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, old_password)
        login.login_assertion()

        settings = Settings(browser)
        settings.go_to_settings_page()
        settings.change_password(new_password)
        settings.password_update_assertion()

        login.submit_logout()
        login.logout_assertion()

        login.go_to_login_page()
        login.login(email, new_password)
        login.login_assertion()
