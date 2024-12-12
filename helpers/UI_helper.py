import pickle
from datetime import datetime, timedelta
import os
import time
import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from faker import Faker
from data.credentials import Credentials

fake = Faker()


class UIHelper:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.credentials = Credentials()

    def open(self):
        with allure.step(f"Open page: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self._PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    def get_current_url(self):
        return self.driver.current_url

    def find(self, locator: tuple) -> WebElement:
        """
        This method helps to find element
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        element = self.wait_for_clickable(locator)
        return element

    def find_all(self, locator: tuple) -> list[WebElement]:
        """
        This method helps to find list of all elements
        :param locator: Not unpacked tuple
        :return: WebElements list
        """
        elements = self.wait_visibility_of_elements(locator)
        return elements

    def fill(self, locator: tuple, text: str):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def make_screenshot(self, name=time.time()):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

    def click_on_element(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def method_click(self, locator):
        locator_type, locator_value = locator
        script = """
                function clickElementByXPath(xpath) {
                    var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (element) {
                        element.click();
                    } else {
                        console.error("Element not found for XPath:", xpath);
                    }
                }
                    clickElementByXPath(arguments[0]);
                    """
        self.driver.execute_script(script, locator_value)



    def load_file(self, locator: tuple, name_file: str):
        file_path = os.path.join(os.getcwd(), 'files', name_file)
        element = self.wait_presence_of_element_located(locator)
        element.send_keys(file_path)

    # --- Waits ---
    def wait_for_visibility(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator), message=message)

    def wait_for_invisibility(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.invisibility_of_element(locator), message=message)

    def wait_for_clickable(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator), message=message)

    def wait_visibility_of_elements(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)

    def wait_and_click(self, locator):
        try:
            button = WebDriverWait(self.driver, 60, poll_frequency=10).until(
                EC.visibility_of_element_located(locator)
            )
            button.click()
        except TimeoutException:
            print(f"Не удалось дождаться видимости элемента: {locator}")

    def wait_presence_of_element_located(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator), message=message)

    # --- Cookies ---
    def save_cookies(self, cookies_name="login-cookies"):
        with open(f"cookies/{cookies_name}.pkl", "wb") as cookies_file:
            pickle.dump(self.driver.get_cookies(), cookies_file)

    def load_cookies(self, cookies_name="login-cookies"):
        with open(f"cookies/{cookies_name}.pkl", "rb") as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

    # --- Scrolls ---
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)

    ## --data generators--

    def fill_date_ant_time_plus_3_min(self, locator_data, locator_time):
        current_date = datetime.now().strftime('%d.%m.%Y')
        time_plus_3_min = (datetime.now() + timedelta(minutes=3)).strftime('%H:%M')
        self.find(locator_data).send_keys(current_date)
        self.find(locator_time).send_keys(time_plus_3_min)

    def fill_date_ant_time_current(self, locator_data, locator_time):
        current_date = datetime.now().strftime('%d.%m.%Y')
        current_time = datetime.now().strftime('%H:%M')
        date_element = self.find(locator_data)
        date_element.send_keys(Keys.CONTROL, 'a')
        date_element.send_keys(Keys.DELETE)
        date_element.send_keys(current_date)
        time_element = self.find(locator_time)
        time_element.send_keys(current_time)

    def fill_date_ant_time_minus_1_min(self, locator_data, locator_time):
        current_date = datetime.now().strftime('%d.%m.%Y')
        time_plus_3_min = (datetime.now() - timedelta(minutes=1)).strftime('%H:%M')
        date_element = self.find(locator_data)
        date_element.send_keys(Keys.CONTROL, 'a')
        date_element.send_keys(Keys.DELETE)
        date_element.send_keys(current_date)
        time_element = self.find(locator_time)
        time_element.send_keys(time_plus_3_min)

    # --- Togglers ---

    def toggle_on(self, locator_checkbox, locator_button):
        element_checkbox = self.find(locator_checkbox)
        if element_checkbox.get_attribute("aria-checked") == "false":
            element_button = self.find(locator_button)
            element_button.click()
        elif element_checkbox.get_attribute("aria-checked") == "true":
            pass

    def toggle_off(self, locator_checkbox, locator_button):
        element_checkbox = self.find(locator_checkbox)
        if element_checkbox.get_attribute("aria-checked") == "true":
            element_button = self.find(locator_button)
            element_button.click()
        elif element_checkbox.get_attribute("aria-checked") == "false":
            pass
