import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка оформления покупки")
@allure.description("Авторизация, добавление товаров, оформление заказа и проверка итоговой суммы")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Открыть страницу авторизации"):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    with allure.step("Ввод логина и пароля"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")

    with allure.step("Нажать кнопку входа"):
        login_page.click_login()

    main_page = MainPage(driver)

    with allure.step("Добавить товары в корзину"):
        main_page.add_item_to_cart("sauce-labs-backpack")
        main_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_item_to_cart("sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        main_page.go_to_cart()

    cart_page = CartPage(driver)

    with allure.step("Нажать Checkout"):
        cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнить форму заказа"):
        checkout_page.enter_firstname("Оксана")
        checkout_page.enter_lastname("Калинина")
        checkout_page.enter_postalcode("400065")
        checkout_page.click_continue()

    with allure.step("Проверить итоговую сумму"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29", f"Ожидалось Total: $58.29, получено {total}"

    driver.quit()
