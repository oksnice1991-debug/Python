import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    @allure.step("Добавление товара в корзину: {item_id}")
    def add_item_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.

        Args:
            item_id (str): Идентификатор товара
            Например, 'sauce-labs-backpack'.

        Returns:
            None
        """
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        Returns:
            None
        """
        self.driver.find_element(*self.cart_icon).click()
