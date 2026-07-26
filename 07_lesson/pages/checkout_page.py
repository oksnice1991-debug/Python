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

    def enter_firstname(self, text):
        self.driver.find_element(*self.firstname).send_keys(text)

    def enter_lastname(self, text):
        self.driver.find_element(*self.lastname).send_keys(text)

    def enter_postalcode(self, text):
        self.driver.find_element(*self.postalcode).send_keys(text)

    def click_continue(self):
        wait = WebDriverWait(self.driver, 10)
        continue_button = wait.until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()
        wait.until(
            EC.presence_of_element_located(self.total_label)
        )

    def get_total(self):
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        return total_element.text
