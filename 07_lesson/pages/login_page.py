from selenium.webdriver.common.by import By


class LoginPage:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, text):
        self.driver.find_element(*self.username).send_keys(text)

    def enter_password(self, text):
        self.driver.find_element(*self.password).send_keys(text)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
