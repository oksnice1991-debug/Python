from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    form_link.click()

    current_url = driver.current_url
    assert current_url.endswith("/forms/post")

    driver.back()

    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
