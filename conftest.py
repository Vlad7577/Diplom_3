import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_page_locators import ConstructorPageLocators


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run tests')


@pytest.fixture
def driver(request):
    browser = request.config.getoption('--browser')
    
    if browser == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Browser {browser} not supported")
    
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    from pages.login_page import LoginPage
    driver.get(Urls.LOGIN_PAGE)
    
    login_page = LoginPage(driver)
    login_page.login(email="vlad-gezik@mail.ru", password="qwerty123")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.PLACE_ORDER_BUTTON)
    )
    return driver