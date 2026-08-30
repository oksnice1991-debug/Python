import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    @allure.step("Добавление товара в корзину: {item_id}")
    def add_item_to_cart(self, item_id):
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
