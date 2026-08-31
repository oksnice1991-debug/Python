from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 60)
    wait.until(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "screen"), "15")
        )

    result_text = driver.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    driver.quit()
