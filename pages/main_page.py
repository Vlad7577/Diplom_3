import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
<<<<<<< HEAD
from urls import BASE_URL
=======
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3


class MainPage(BasePage):

<<<<<<< HEAD
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)
=======
    URL = "https://stellarburgers.education-services.ru/"

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(self.URL)
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3

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

<<<<<<< HEAD
    @allure.step("Проверить отображение модального окна")
    def is_modal_visible(self):
        return self.find_element(MainPageLocators.MODAL)

    @allure.step("Получить значение счётчика ингредиента")
    def get_counter(self):
        counter = self.get_text(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter)

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient(self):

        ingredient = self.find_element(MainPageLocators.INGREDIENT)
        constructor = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)

        self.driver.execute_script("""
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                };
                return event;
            }

            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }

            function simulateHTML5DragAndDrop(element, destination) {
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(element, dragStartEvent);

                var dropEvent = createEvent('drop');
                dispatchEvent(destination, dropEvent, dragStartEvent.dataTransfer);

                var dragEndEvent = createEvent('dragend');
                dispatchEvent(element, dragEndEvent, dropEvent.dataTransfer);
            }

            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """, ingredient, constructor)

    @allure.step("Проверить отображение конструктора")
    def is_constructor_visible(self):
        return self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверить отображение ленты заказов")
    def is_order_feed_visible(self):
        return self.find_element(MainPageLocators.ORDER_FEED_BUTTON)
=======
    @allure.step("Получить счетчик ингредиента")
    def get_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
