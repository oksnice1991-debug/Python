from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    SCREEN = (By.CLASS_NAME, "screen")
    delay_input = (By.ID, "delay")

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, text):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def wait_for_result(self, expected, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
            )

    def get_result_text(self):
        return self.driver.find_element(*self.SCREEN).text
