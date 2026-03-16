import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    @allure.step('Ожидание загрузки страницы "Лента заказов"')
    def wait_for_order_feed_load(self):
        self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_HEADER)
    
    @allure.step('Получение количества выполненных заказов за всё время')
    def get_completed_all_time(self):
        return int(self.get_text(OrderFeedLocators.COMPLETED_ALL_TIME))
    
    @allure.step('Получение количества выполненных заказов за сегодня')
    def get_completed_today(self):
        return int(self.get_text(OrderFeedLocators.COMPLETED_TODAY))
    
    @allure.step('Получение списка заказов в работе')
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]
    
    @allure.step('Клик по первому заказу в ленте')
    def click_first_order(self):
        self.click_element(OrderFeedLocators.ORDER_CARD)

    @allure.step('Открыть страницу ленты заказов')
    def open_url_of_order_feed(self):
        from urls import Urls
        self.driver.get(Urls.ORDER_FEED)

    @allure.step('Проверить отображение страницы ленты заказов')
    def check_order_feed_page_displaying(self):
        return self.find_element(OrderFeedLocators.ORDER_FEED_HEADER).is_displayed()

    @allure.step('Получить текст из элемента с заказами в работе')
    def get_text_from_element_orders_in_progress(self):
        return self.get_text(OrderFeedLocators.ORDERS_IN_PROGRESS)

    @allure.step('Получить список заказов в работе')
    def get_orders_list(self):
        orders_text = self.get_text_from_element_orders_in_progress()
    
        import re
        orders_list = re.findall(r'\d+', orders_text)
    
        return orders_list