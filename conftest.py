import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("-window-size=1920, 1080")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture
def soap_config():
    if os.environ["STAGE"] == "brusnika-qa":
        return {
            "url": "https://brusnika-qa.demo.ultimeta.ru/ws/brusnika-1c",
            "headers": {"Content-Type": "text/xml; charset=utf-8"},
            "auth": ("test", "test")
        }
    elif os.environ["STAGE"] == "brusnika":
        return {
            "url": "https://brusnika.demo.ultimeta.ru/ws/brusnika-1c",
            "headers": {"Content-Type": "text/xml; charset=utf-8"},
            "auth": ("test", "test")
        }