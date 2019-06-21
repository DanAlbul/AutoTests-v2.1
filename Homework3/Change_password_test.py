from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pages.Login_page import Login
from Pages.Settings_page import Settings

class ChangePasswordTest():

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def ChangePassswordTest(self):
        driver = self.driver
        driver.get("https://anotepad.com/create_account")
        driver.maximize_window()
        email = "kair317@gmail.com"
        old_password = "1234567"
        new_password = "7777611"

        login = Login(driver)
        login.login(email, old_password).login_assertion()

        settings = Settings(driver)
        settings.go_to_settings_page().change_password(new_password).password_update_assertion()

        login.submit_logout().logout_assertion()

        login.go_to_login_page().login(email, new_password).login_assertion()

    def tearDown(self):
        self.driver.quit()