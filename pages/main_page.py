import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    URL = "https://stellarburgers.education-services.ru/"

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(self.URL)

    @allure.step("Перейти в Конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в Ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Открыть ингредиент")
    def open_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Получить счетчик ингредиента")
    def get_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)