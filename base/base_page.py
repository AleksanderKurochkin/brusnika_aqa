from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclasses=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)

    def open(self):
        self.driver.get(self._PAGE_URL)


    def click_on_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    # Ввод текста
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    def enter_text_and_click(self, locator_field, text, locator_value):
        self.enter_text(locator_field, text)
        self.click_on_element(locator_value)
