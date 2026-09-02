from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Оксана")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
        )
    submit_button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("/post"))
    assert "/post" in driver.current_url

    driver.quit()
