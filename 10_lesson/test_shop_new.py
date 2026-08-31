import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка сценария оформления покупки")
@allure.description("Авторизация, добавление трех товаров"
                    "оформление заказа и проверка итоговой суммы")
@allure.feature("Оформление заказа")
@allure.severity("blocker")
def test_shop():
    with allure.step("Открыть страницу авторизации"):
        driver = webdriver.Chrome()
        driver.get(
            "https://www.saucedemo.com/"
            )
    with allure.step("Ввод логина и пароля"):
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
    with allure.step("Нажать кнопку входа"):
        login_page.click_login()
    with allure.step("Добавить 3 товара в корзину"):
        main_page = MainPage(driver)
        main_page.add_item_to_cart("sauce-labs-backpack")
        main_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_item_to_cart("sauce-labs-onesie")
    with allure.step("Переход в корзину"):
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()
    with allure.step("Заполнение формы заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_firstname("Oksana")
        checkout_page.enter_lastname("Kalinina")
        checkout_page.enter_postalcode('400065')
        checkout_page.click_continue()
    with allure.step("Проверка итоговой суммы"):
        result = checkout_page.get_total()
        assert result == "Total: $58.29", (
            f"Ожидалось Total: $58.29, получено {result}"
            )

    driver.quit()
