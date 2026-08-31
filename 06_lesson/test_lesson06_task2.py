from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get(" https://gitflic.ru/")

    user1_cookie = {
        "name": "session",
        "value":
        "NDZlZTI2MjUtYWI4MC00Nzc5LWJhMzAtYmUwZTgzYWJjNDJh"
        }

    user2_cookie = {
        "name": "session",
        "value":
        "NmJjYzY5ZTItZWJhYi00YzVjLTg0ZjAtYWE4MjA4NzkwODI5"
        }

    driver.add_cookie(user1_cookie)
    driver.refresh()
    driver.get("https://gitflic.ru/user/doksana")
    url1 = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie(user2_cookie)
    driver.refresh()
    driver.get("https://gitflic.ru/user/dubovskayabakery")
    url2 = driver.current_url

    assert url1 != url2
    driver.quit()
    