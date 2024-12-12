
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("-window-size=1920, 1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()