import pytest

from Pages.Login_page import Login
from Pages.Home_page import HomePage
from Pages.Settings_page import Settings

link = 'https://anotepad.com/create_account'

class TestClass(object):

# TC GL-894:Login into the app -----------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        'email, password', [
            ('kair317@gmail.com', '1234567'),                       # valid email and password ... Expected: PASS
            ('invalid9384569834@hotmail.com', 'notvalidpas34091')   # invalid email and password ... Expected: FAIL
        ]
    )
    def test_login(self, browser, email, password):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
        login.login_assertion()
        login.submit_logout()
        login.logout_assertion()

# TC GL-805:Saving notes as "Private" or "Public" (only for registered users) ------------------------------------------
    @pytest.mark.parametrize(
        'email, password, note', [
            ('kair317@gmail.com', '1234567', 'FNote 3'),            # valid note ... Expected: PASS
            ('kair317@gmail.com', '1234567', 'Non-existing note')   # invalid note ... Expected: FAIL
        ]
    )
    def test_public_or_private_save(self, browser, email, password, note):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
        login.login_assertion()

        home_page = HomePage(browser)
        # public
        home_page.select_note(note)
        home_page.public_or_private_setting()
        home_page.public_checkbox()
        home_page.public_selected_assert()

        # private
        home_page.select_note(note)
        home_page.public_or_private_setting()
        home_page.private_checkbox()
        home_page.private_selected_assert()

# TC GL-897:Changing a password ----------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        'email, password, new_password', [
            ('kair317@gmail.com', '1234567', '7777611'),    # valid password ... Expected: PASS
            ('danielvpace@gmail.com', 'qwerty', '575')      # invalid password ... Expected: FAIL
        ]
    )
    def test_change_password(self, browser, email, password, new_password):
        browser.get(link)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
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
