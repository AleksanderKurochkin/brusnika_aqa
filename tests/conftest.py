from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="function", autouse=True) #scope="function" создает браузер для каждого теста отдельно
                                                # autouse=True Позволяет использовать для каждого автотеста не вызывая фикстуру
def browser_chrom(request):
    options = Options()
    #options.add_argument("--headless") # безголовый режим
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  # Передача экземпляра драйвера в тестовый класс
    yield driver
    driver.quit()