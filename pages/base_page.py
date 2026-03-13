<<<<<<< HEAD
import allure
=======
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

<<<<<<< HEAD
    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
=======
    def open(self, url):
        self.driver.get(url)

>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

<<<<<<< HEAD
    @allure.step("Клик по элементу")
=======
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

<<<<<<< HEAD
    @allure.step("Получить текст элемента")
=======
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
    def get_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text