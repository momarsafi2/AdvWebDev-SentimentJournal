import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_homepage_e2e():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://localhost:5000")
        time.sleep(1)

        assert "Mood" in driver.title or "Journal" in driver.title

    finally:
        driver.quit()
