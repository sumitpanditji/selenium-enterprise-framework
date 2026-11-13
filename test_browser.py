from selenium import webdriver
from selenium.webdriver.common.by import By

def test_browser_launch():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.selenium.dev")

        assert "Selenium" in driver.title

        print("Broswer automation successful")

    finally:
        driver.quit()