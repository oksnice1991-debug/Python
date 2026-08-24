from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Chrome()
    driver.get(
        "https://www.saucedemo.com/"
        )
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    main_page = MainPage(driver)
    main_page.add_item_to_cart("sauce-labs-backpack")
    main_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_item_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_firstname("Oksana")
    checkout_page.enter_lastname("Kalinina")
    checkout_page.enter_postalcode('400065')
    checkout_page.click_continue()
    result = checkout_page.get_total()
    assert result == "Total: $58.29", (
        f"Ожидалось Total: $58.29, получено {result}"
    )

    driver.quit()
