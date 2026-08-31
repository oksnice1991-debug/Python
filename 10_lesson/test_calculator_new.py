import allure
from selenium import webdriver
from pages.calc_page import CalcPage


@allure.title("Проверка калькулятора с задержкой")
@allure.description("Установка задержки 45 секунд,"
                    "ввод 7+8=, проверка результата 15")
@allure.feature("Калькулятор")
@allure.severity("blocker")
def test_calculator():
    with allure.step("Открыть страницу калькулятора"):
        driver = webdriver.Chrome()
        driver.get(
            "https://bonigarcia.dev/selenium-"
            "webdriver-java/slow-calculator.html"
        )
    calc_page = CalcPage(driver)
    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)
    with allure.step("Ввести 7+8="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")
    with allure.step("Дождаться результата 15"):
        calc_page.wait_for_result("15")
    with allure.step("Проверить результат"):
        result = calc_page.get_result_text()
        assert result == "15", f"Ожидалось 15б получено {result}"

    driver.quit()
