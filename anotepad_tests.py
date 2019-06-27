import pytest
import allure_pytest
import allure
from Pages.Login_page import Login
from Pages.Home_page import HomePage
from Pages.Settings_page import Settings

AUT_LINK = 'https://anotepad.com/create_account'

class TestClass(object):

    TC_LINK = 'http://52.169.88.152/lib/testcases/tcPrint.php?show_mode=&testcase_id=5141&tcversion_id=5142'
    @allure.testcase(TC_LINK, "Test Case: GL-894:Login into the app")
    @allure.feature("Logging in")
    @pytest.mark.parametrize(
        'email, password', [
            ('kair317@gmail.com', '1234567'),                       # valid email and password ... Expected: PASS
            ('invalid9384569834@hotmail.com', 'notvalidpas34091')   # invalid email and password ... Expected: FAIL
        ]
    )
  # @pytest.mark.withallure
    def test_login(self, browser, email, password):
        browser.get(AUT_LINK)
        browser.maximize_window()

        login = Login(browser)
        login.login(email, password)
        login.login_assertion()
        login.submit_logout()
        login.logout_assertion()


    TC_LINK = 'http://52.169.88.152/lib/testcases/tcPrint.php?show_mode=&testcase_id=4567&tcversion_id=4568'
    @allure.testcase(TC_LINK, "Test Case: GL-805:Saving notes as 'Private' or 'Public' (only for registered users)")
    @allure.feature("Saving notes with Public or Private access")
    @pytest.mark.parametrize(
        'email, password, note', [
            ('kair317@gmail.com', '1234567', 'FNote 3'),            # valid note ... Expected: PASS
            ('kair317@gmail.com', '1234567', 'Non-existing note')   # invalid note ... Expected: FAIL
        ]
    )
    def test_public_or_private_save(self, browser, email, password, note):
        browser.get(AUT_LINK)
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

    TC_LINK = 'http://52.169.88.152/lib/testcases/tcPrint.php?show_mode=&testcase_id=5157&tcversion_id=5158'
    @allure.testcase(TC_LINK, "Test Case: GL-897:Changing a password")
    @allure.feature("Changing an account password")
    @pytest.mark.parametrize(
        'email, password, new_password', [
            ('kair317@gmail.com', '1234567', '7777611'),    # valid password ... Expected: PASS
            ('danielvpace@gmail.com', 'qwerty', '575')      # invalid password ... Expected: FAIL
        ]
    )
    def test_change_password(self, browser, email, password, new_password):
        browser.get(AUT_LINK)
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
