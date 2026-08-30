import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.button_checkout = (By.CSS_SELECTOR, "[data-test='checkout']")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self):
        self.driver.find_element(*self.button_checkout).click()
