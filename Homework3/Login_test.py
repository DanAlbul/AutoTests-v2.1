import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login_page import Login
from Pages.Home_page import HomePage

link = 'https://anotepad.com/create_account'
email = "kair317@gmail.com"
password = "1234567"


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    browser.quit()

class TestLogin(object):

    def test_login(self, browser):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
        login.login_assertion()
        login.submit_logout()
        login.logout_assertion()
