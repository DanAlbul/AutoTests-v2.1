from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pages.Login_page import Login
from Pages.Home_page import HomePage
from Pages.Settings_page import Settings

class ChangePasswordTest():

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def SaveAsPublicOrPrivateTest (self):
        driver = self.driver
        driver.get("https://anotepad.com/create_account")
        driver.maximize_window()
        email = "kair317@gmail.com"
        password = "1234567"

        login = Login(driver)
        login.login(email, password).login_assertion().submit_logout().logout_assertion()

        home_page = HomePage(driver)
        home_page.select_note("FNote 3").public_or_private_setting().public_checkbox().public_selected_assert()
        home_page.select_note("FNote 3").public_or_private_setting().private_checkbox().private_selected_assert()

    def tearDown(self):
        self.driver.quit()