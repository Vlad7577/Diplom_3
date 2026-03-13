import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

<<<<<<< HEAD
    def __init__(self, driver):
        super().__init__(driver)

=======
>>>>>>> 7be5eb6b022f54b90bee01de82e37b26eebf1ee3
    @allure.step("Получить счетчик выполнено за всё время")
    def get_total_counter(self):
        return self.get_text(OrderFeedLocators.TOTAL_COUNTER)

    @allure.step("Получить счетчик выполнено за сегодня")
    def get_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    @allure.step("Проверить наличие заказов в работе")
    def get_orders_in_progress(self):
        return self.find_element(OrderFeedLocators.ORDER_IN_PROGRESS)