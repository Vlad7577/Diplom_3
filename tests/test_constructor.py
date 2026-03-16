import allure
from pages.constructor_page import ConstructorPage


@allure.feature("Конструктор")
class TestConstructor:
    
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        page = ConstructorPage(driver)
        initial_url = page.get_current_url()
        
        page.click_order_feed()
        page.click_constructor()
        
        assert page.get_current_url() == initial_url
    
    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed(self, driver):
        page = ConstructorPage(driver)
        
        page.click_order_feed()
        
        assert "feed" in page.get_current_url()
