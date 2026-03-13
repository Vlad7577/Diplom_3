import allure
from pages.main_page import MainPage


class TestConstructor:

    @allure.title("Переход в раздел Конструктор")
    def test_constructor_section(self, driver):

        page = MainPage(driver)
        page.open_main_page()

        page.click_constructor()

        assert page.is_constructor_visible()


    @allure.title("Переход в раздел Лента заказов")
    def test_order_feed_section(self, driver):

        page = MainPage(driver)
        page.open_main_page()

        page.click_order_feed()

        assert page.is_order_feed_visible()


    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):

        page = MainPage(driver)
        page.open_main_page()

        page.open_ingredient()

        assert page.is_modal_visible()


    @allure.title("Закрытие модального окна ингредиента")
    def test_close_modal(self, driver):

        page = MainPage(driver)
        page.open_main_page()

        page.open_ingredient()
        page.close_modal()

        assert page.is_constructor_visible()


    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter(self, driver):

        page = MainPage(driver)
        page.open_main_page()

        counter_before = int(page.get_counter())

        page.drag_ingredient()

        counter_after = int(page.get_counter())

        assert counter_after > counter_before