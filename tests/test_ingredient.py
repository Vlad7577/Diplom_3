import allure
from pages.constructor_page import ConstructorPage


@allure.feature("Ингредиенты")
class TestIngredient:
    
    @allure.title("Клик на ингредиент открывает всплывающее окно")
    def test_ingredient_modal_appears(self, driver):
        page = ConstructorPage(driver)
        
        page.click_ingredient()
        
        assert page.is_ingredient_modal_displayed()
    
    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_modal(self, driver):
        page = ConstructorPage(driver)
        
        page.click_ingredient()
        page.close_modal()
        
        assert page.is_modal_closed()
    
    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver)
        
        initial_count = page.get_ingredient_counter()
        page.add_ingredient_to_order()
        new_count = page.get_ingredient_counter()
        
        assert new_count == initial_count + 2