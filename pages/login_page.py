import allure
from pages.base_page import BasePage
from data import UserData
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step('Вход в личный кабинет')
    def login(self, email=UserData.EMAIL, password=UserData.PASSWORD):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)