import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    SCREEN = (By.CLASS_NAME, "screen")
    delay_input = (By.ID, "delay")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Установка задержки: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку перед вычислением.

        Args:
            seconds (int):  Количество секунд задержки.

        Returns:
            None
        """
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(str(seconds))

    @allure.step("Нажатие кнопки: {text}")
    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора с указанным текстом.

        Args:
            text (str): Текст на кнопке (например, '7', '+', '=').

        Returns:
            None
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    @allure.step("Ожидание результата: {expected}")
    def wait_for_result(self, expected: str, timeout: int = 60) -> None:
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        Args:
            expected (str): Ожидаемый текст результата.
            timeout (int): Максимальное время ожидания в секундах.

        Returns:
            None
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.SCREEN, expected))

    @allure.step("Получение результата")
    def get_result_text(self) -> str:
        """
        Возвращает текст результата с экрана калькулятора.

        Returns:
            str: Текст результата.
        """
        return self.driver.find_element(*self.SCREEN).text
