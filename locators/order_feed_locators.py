from selenium.webdriver.common.by import By

class OrderFeedLocators():

    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    ORDER_CARD = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")