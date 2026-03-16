import allure
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title('Проверка увеличения счетчика "Выполнено за все время" после создания заказа')
    def test_completed_all_time_increases(self, authenticated_driver):

        order_feed_page = OrderFeedPage(authenticated_driver)
        constructor_page = ConstructorPage(authenticated_driver)
        base_page = BasePage(authenticated_driver)

        order_feed_page.open_url_of_order_feed()
        counter_before = base_page.get_text(OrderFeedLocators.COMPLETED_ALL_TIME)

        constructor_page.click_constructor()
        constructor_page.create_order()
        constructor_page.close_modal()

        constructor_page.click_order_feed()
        counter_after = base_page.get_text(OrderFeedLocators.COMPLETED_ALL_TIME)

        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" после создания заказа')
    def test_completed_today_increases(self, authenticated_driver):
        order_feed_page = OrderFeedPage(authenticated_driver)
        constructor_page = ConstructorPage(authenticated_driver)
        base_page = BasePage(authenticated_driver)

        order_feed_page.open_url_of_order_feed()
        counter_before = base_page.get_text(OrderFeedLocators.COMPLETED_TODAY)

        constructor_page.click_constructor()
        constructor_page.create_order()
    
        constructor_page.click_order_feed()

        counter_after = base_page.get_text(OrderFeedLocators.COMPLETED_TODAY)
        assert int(counter_after) > int(counter_before)

    @allure.title('Проверка добавления номера заказа в раздел "В работе" после его создания')
    def test_order_in_progress_after_creation(self, authenticated_driver):
        constructor_page = ConstructorPage(authenticated_driver)
        order_feed_page = OrderFeedPage(authenticated_driver)
    
        constructor_page.click_order_feed()
        order_feed_page.wait_for_order_feed_load()
        count_before = len(order_feed_page.get_orders_list())
    
        constructor_page.click_constructor()
        constructor_page.create_order()
    
        constructor_page.click_order_feed()
        order_feed_page.wait_for_order_feed_load()
        count_after = len(order_feed_page.get_orders_list())
        assert count_after == count_before + 1