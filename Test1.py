import time
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeDriverManager
# from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Edge(executable_path=EdgeDriverManager().install())
# driver = webdriver.Ie(executable_path=IEDriverManager().install())

driver.get("https://anotepad.com/create_account")
email = driver.find_element_by_id("loginEmail").send_keys("kair317@gmail.com")
password = driver.find_element_by_css_selector('#password[placeholder*="Enter"]').send_keys("1234567" + Keys.ENTER)
note = driver.find_element_by_css_selector('a[title*="1233121"]')
note.click()
deleteBtn = driver.find_element_by_class_name("delete").click()
time.sleep(2)
driver.switch_to.alert.accept()
