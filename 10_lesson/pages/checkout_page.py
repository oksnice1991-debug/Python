import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    postalcode = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    total_label = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввод имени: {text}")
    def enter_firstname(self, text: str) -> None:
        """Вводит имя в поле first-name"""
        self.driver.find_element(*self.firstname).send_keys(text)

    @allure.step("Ввод фамилии: {text}")
    def enter_lastname(self, text: str) -> None:
        """Вводит фамилию в поле last-name"""
        self.driver.find_element(*self.lastname).send_keys(text)

    @allure.step("Ввод почтового индекса: {text}")
    def enter_postalcode(self, text: str) -> None:
        """Вводит почтовый индекс в поле postal-code"""
        self.driver.find_element(*self.postalcode).send_keys(text)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        """Нажимает кнопку Continue и ждёт появления итоговой суммы"""
        wait = WebDriverWait(self.driver, 10)
        continue_button = wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()
        wait.until(
            EC.presence_of_element_located(self.total_label)
        )

    @allure.step("Получение итоговой суммы")
    def get_total(self) -> None:
        """Возвращает текст итоговой суммы"""
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        return total_element.text
