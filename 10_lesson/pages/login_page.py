import allure
from selenium.webdriver.common.by import By


class LoginPage:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввод логина: {text}")
    def enter_username(self, text: str) -> None:
        """
        Вводит логин в поле username.

        Args:
            text (str): Логин пользователя.

        Returns:
            None
        """
        self.driver.find_element(*self.username).send_keys(text)

    @allure.step("Ввод пароля")
    def enter_password(self, text: str) -> None:
        """
        Вводит пароль в поле password.

        Args:
            text (str): Пароль пользователя.

        Returns:
            None
        """
        self.driver.find_element(*self.password).send_keys(text)

    @allure.step("Нажатие кнопки входа")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа.

        Returns:
            None
        """
        self.driver.find_element(*self.login_button).click()
