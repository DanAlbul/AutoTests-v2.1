import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@allure.step("Open a browser")
def open_browser():
    pass

@allure.step("Close a browser")
def close_browser():
    pass

@pytest.fixture(scope="session", autouse=True)
def browser():
    open_browser()
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield browser
    close_browser()
    browser.quit()
