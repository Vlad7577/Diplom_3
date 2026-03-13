import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()