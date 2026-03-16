from selenium.webdriver.common.by import By

class ConstructorPageLocators():
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/']")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    BUN_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter')]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")