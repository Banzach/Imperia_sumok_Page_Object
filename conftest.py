import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



#Fixture: open browser with our options
#@pytest.fixture(scope="function")
#def browser(request):
#
#   print("\nstart chrome browser for test..")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nquit browser..")
#    browser.quit()