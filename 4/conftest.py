import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
#    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    print("\nlanguage:%s" % language)
    yield browser
    print("\nquit browser..")
    browser.quit()