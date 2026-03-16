import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получить текст")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание отсутствия видимости элемента")
    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Удалить все модальные окна')
    def remove_all_modals(self):
        self.driver.execute_script()
        
    @allure.step('Закрыть модальное окно через скрипт')
    def safe_click(self, locator, timeout =10):
        elements = WebDriverWait(self.driver, timeout).until(
        lambda d: d.find_elements(*locator)
        )
    
        visible_element = None
        for element in elements:
            if element.is_displayed():
                visible_element = element
                break
    
        if visible_element:
  
            self.driver.execute_script("arguments[0].click();", visible_element)
        else:
            raise Exception(f"Нет видимых элементов по локатору {locator}")
        
    @allure.step('Клик через JavaScript')
    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)