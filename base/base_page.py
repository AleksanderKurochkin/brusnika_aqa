from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        self.action = ActionChains(driver)

    # def choose_from_list(self, locator_field, text, locator_value):
    #     field = self.wait.until(EC.element_to_be_clickable(locator_field))
    #     field.send_keys(text)
    #     choose_value = self.wait.until(EC.element_to_be_clickable(locator_value))
    #     self.action.click(choose_value).perform()

    def click_on_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def open_page(self, url):
        self.driver.get(url)

    # Ввод текста
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    def enter_text_and_click(self, locator_field, text, locator_value):
        self.enter_text(locator_field, text)
        self.click_on_element(locator_value)
