import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "[data-test='checkout']")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку Checkout для перехода к оформлению заказа.

        Returns:
            None
        """
        self.driver.find_element(*self.checkout_button).click()
