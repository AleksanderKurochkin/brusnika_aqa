from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.get_attribute("textContent")

    def get_current_url(self):
        return self.driver.current_url

    def url_with_wait(self, url):
        self.wait.until(EC.url_to_be(url))
        return url

    def open_page(self, url):
        self.driver.get(url)

    def check_url(self, actual_url, expected_url):
        return actual_url == expected_url

    #Ввод текста
    def enter_text(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def visibl_display(self, locator):
        self.find_element_with_wait(locator)

    def find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

