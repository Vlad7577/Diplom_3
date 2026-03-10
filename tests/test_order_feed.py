import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.title("Проверка счетчика выполнено за всё время")
def test_total_orders_counter(driver):

    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    main_page.open_main_page()
    main_page.click_order_feed()

    total = order_feed_page.get_total_counter()

    assert int(total) >= 0


@allure.title("Проверка счетчика выполнено за сегодня")
def test_today_orders_counter(driver):

    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    main_page.open_main_page()
    main_page.click_order_feed()

    today = order_feed_page.get_today_counter()

    assert int(today) >= 0


@allure.title("Проверка наличия заказов в работе")
def test_orders_in_progress(driver):

    main_page = MainPage(driver)
    order_feed_page = OrderFeedPage(driver)

    main_page.open_main_page()
    main_page.click_order_feed()

    order = order_feed_page.get_orders_in_progress()

    assert order is not None