from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Pages.Login_page import Login

class LoginTest():

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def LoginTest(self):
        driver = self.driver
        driver.get("https://anotepad.com/create_account")
        driver.maximize_window()
        email = "kair317@gmail.com"
        password = "1234567"

        login = Login(driver)
        login.login(email, password).login_assertion().submit_logout().logout_assertion()

    def tearDown(self):
        self.driver.quit()