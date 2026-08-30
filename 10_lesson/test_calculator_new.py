import allure
from selenium import webdriver
from pages.calc_page import CalcPage


@allure.title("Проверка калькулятора с задержкой")
@allure.description("Установка задержки 45 секунд,"
                    "ввод 7+8=, проверка результата 15")
@allure.feature("Калькулятор")
@allure.severity("blocker")
def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    calc_page = CalcPage(driver)

    calc_page.set_delay(45)
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result("15")
    result = calc_page.get_result_text()
    assert result == "15", f"Ожидалось 15б получено {result}"

    driver.quit()
