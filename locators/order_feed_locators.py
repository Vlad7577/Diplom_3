from selenium.webdriver.common.by import By

class OrderFeedLocators:

    TOTAL_COUNTER = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[1]")

    TODAY_COUNTER = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[2]")

    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//li")