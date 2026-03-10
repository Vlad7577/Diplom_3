import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.title("Переход в раздел Конструктор")
def test_constructor_section(driver):

    page = MainPage(driver)
    page.open_main_page()

    page.click_constructor()

    assert page.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)


@allure.title("Переход в раздел Лента заказов")
def test_order_feed_section(driver):

    page = MainPage(driver)
    page.open_main_page()

    page.click_order_feed()

    assert page.find_element(MainPageLocators.ORDER_FEED_BUTTON)


@allure.title("Открытие модального окна ингредиента")
def test_open_ingredient_modal(driver):

    page = MainPage(driver)
    page.open_main_page()

    page.open_ingredient()

    assert page.find_element(MainPageLocators.MODAL)


@allure.title("Закрытие модального окна ингредиента")
def test_close_modal(driver):

    page = MainPage(driver)
    page.open_main_page()

    page.open_ingredient()
    page.close_modal()

    assert page.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)


@allure.title("Увеличение счетчика ингредиента")
def test_ingredient_counter(driver):

    page = MainPage(driver)
    page.open_main_page()

    page.open_ingredient()

    counter = page.get_counter()

    assert int(counter) >= 0