import time
from selenium.common import NoSuchElementException
from base.base_page import BasePage
import allure

class PurchasePageOrganizer(BasePage):
    # _PAGE_URL = None
    _PAGE_URL = ("https://brusnika-qa.demo.ultimeta.ru/trades/100808934/info")

    _BUTTON_RESULT = "//span[text() = 'Подвести итоги']"
    _BUTTON_EDIT_PURCHASE = "//span[text() = 'Внести изменения']"
    _BUTTON_EDIT = "//span[text() = 'Изменить']"
    _BUTTON_APPOINT_TK = "//span[text() = 'Назначить состав ТК']"
    _BUTTON_APPOINT_TK_DIALOG = "//mat-dialog-actions//span[contains(text(), 'Назначить состав ТК')]"
    _BUTTON_STATEMENT = "//span[contains(text(), 'Перейти к утверждению')]"
    _BUTTON_CHOOSE_WINNER = "//span[contains(text(), 'Определить победителей')]"
    _FIELD_CHOOSE_WINNER = "//mat-select"
    _CHOOSE_WINNER = "//span[text() = 'Автоматически по общей сумме']"

    _FIELD_CHOOSE_TK = "//mat-select[@id=(//mat-label[contains(text(), 'Выберите комиссию')]/ancestor::label/@for)]"
    _TK_DEMO_ONE = "//span//div[contains(text(), 'Демо коммисия 1')]"

    def get_url_purchase(self):
        with allure.step(f"Получаем ID закупки: {self._PAGE_URL}"):
            current_url = self.get_current_url()
            self._PAGE_URL = "/".join(current_url.split("/")[:5])  # Берем первые 5 частей URL
            return self._PAGE_URL

    def wait_button_result(self):
        locator = self._BUTTON_RESULT
        try:
            button = self.find(locator)
            if button.is_displayed():
                button.click()
            else:
                self.wait_and_click(locator)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    @allure.step("Нажать кнопку 'изменить закупку' в карточке закупки")
    def open_edit_purchase(self):
        self.click_on_element(self._BUTTON_EDIT_PURCHASE)

    @allure.step("Нажать кнопку изменить (карточку закупки)")
    def click_edit_purchase(self):
        self.click_on_element(self._BUTTON_EDIT)

    @allure.step("Нажать кнопку 'Подвести итоги'")
    def click_button_result(self):
        self.click_on_element(self._BUTTON_RESULT)

    @allure.step("Нажать кнопку 'Назначить состав ТК'")
    def click_button_appoint_tk(self):
        self.click_on_element(self._BUTTON_APPOINT_TK)

    @allure.step("Выбрать коммисию ТК Демо коммисия 1")
    def choose_tk(self):
        self.click_on_element(self._FIELD_CHOOSE_TK)
        self.click_on_element(self._TK_DEMO_ONE)
        self.click_on_element(self._BUTTON_APPOINT_TK_DIALOG)

    @allure.step("Нажать кнопку 'Перейти к утверждению'")
    def click_button_statement(self):
        self.click_on_element(self._BUTTON_STATEMENT)

    @allure.step("Нажать кнопку 'Определить победителей'")
    def click_button_choose_winner(self):
        self.click_on_element(self._BUTTON_CHOOSE_WINNER)

    @allure.step("Выбор победителя 'Автоматически по общей сумме'")
    def choose_winner(self):
        self.click_on_element(self._FIELD_CHOOSE_WINNER)
        self.click_on_element(self._CHOOSE_WINNER)










