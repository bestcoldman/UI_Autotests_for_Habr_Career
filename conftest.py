import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)

def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (NoSuchElementException):
        return False
    return True
