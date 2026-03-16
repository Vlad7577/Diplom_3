import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from locators.constructor_page_locators import ConstructorPageLocators

class ConstructorPage(BasePage):
    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor(self):
        self.click_element(ConstructorPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step('Клик на кнопку "Лента заказов"')
    def click_order_feed(self):
        self.js_click(ConstructorPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик на ингредиент (булка)')
    def click_ingredient(self):
        self.click_element(ConstructorPageLocators.BUN_INGREDIENT)
    
    @allure.step('Проверка отображения модального окна с деталями ингредиента')
    def is_ingredient_modal_displayed(self):
        self.find_element(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL).is_displayed()
        return self.find_element(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL).is_displayed()

    @allure.step('Закрытие модального окна')
    def close_modal(self):
        self.safe_click(ConstructorPageLocators.CLOSE_MODAL_BUTTON)
    
    @allure.step('Проверка, что модальное окно закрыто')
    def is_modal_closed(self):
        self.wait_for_element_invisible(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL)
        return True
        
    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_counter(self):
        element = self.wait.until(EC.visibility_of_element_located(ConstructorPageLocators.BUN_COUNTER))
        return int(element.text)
    
    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        ingredient = self.find_element(ConstructorPageLocators.BUN_INGREDIENT)
        constructor = self.find_element(ConstructorPageLocators.BURGER_CONSTRUCTOR)
    
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()

    
    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_place_order_button(self):
        self.find_element(ConstructorPageLocators.PLACE_ORDER_BUTTON)
        self.click_element(ConstructorPageLocators.PLACE_ORDER_BUTTON)
    
    @allure.step('Получение номера заказа из модального окна')
    def get_order_number(self):
        self.wait_for_element_visible(ConstructorPageLocators.ORDER_NUMBER_MODAL)
        return self.get_text(ConstructorPageLocators.ORDER_NUMBER_MODAL)
    
    @allure.step('Клик на кнопку "Войти в аккаунт" на главной')
    def click_login_button(self):
        self.click_element(ConstructorPageLocators.LOGIN_BUTTON_MAIN)

    @allure.step('Создать заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_place_order_button()
        order_number = self.get_order_number()
        return order_number