import time
from base.base_page import BasePage
import allure


class PurchasePageOrganizer(BasePage):
    _PAGE_URL = None
    _PAGE_URL = ("https://brusnika-qa.demo.ultimeta.ru/trades/100810129")

    _BUTTON_RESULT = "//span[text() = 'Подвести итоги']"
    _BUTTON_EDIT_PURCHASE = "//span[text() = 'Внести изменения']"
    _BUTTON_EDIT = "//span[text() = 'Изменить']"
    _BUTTON_APPOINT_TK = "//span[text() = 'Назначить состав ТК']"
    _BUTTON_CENCEL = "//span[text() = 'Отмена']"
    _BUTTON_APPOINT_TK_DIALOG = "//mat-dialog-actions//span[contains(text(), 'Назначить состав ТК')]"
    _BUTTON_STATEMENT = "//span[contains(text(), 'Перейти к утверждению')]"
    _BUTTON_CHOOSE_WINNER = "//span[contains(text(), 'Определить победителей')]"
    _BUTTON_SAVE_AND_APPROVE = "//span[text() = 'Сохранить и утвердить']"
    _BUTTON_APPROVE_RESULTS_VOTE = "//span[contains(text(), 'Утвердить результаты голосования')]"
    _BUTTON_APPROVE_PROTOCOL_RESULTS = "//span[contains(text(), 'Утвердить протокол итогов этапа')]"
    _BUTTON_APPROVE = "//button[.//span[contains(text(), 'Утвердить')]]"
    _BUTTON_MENU = "//span[text()='Голосование']/ancestor::span[contains(@class, 'mat-button-wrapper')]//mat-icon"
    _FIELD_CHOOSE_WINNER = "//mat-select//span[contains(text(), 'Вручную')]"
    _FIELD_FINAL_CONCLUSION = '//mat-form-field//textarea'
    _CHOOSE_WINNER = "//span[text() = 'Автоматически по общей сумме']"
    _FIELD_MEMBER_COMMITTEE = "//input[@id='mat-chip-list-input-2']"
    _FIELD_CHAIRMAN_COMMITTEE = "//um-combo-box-field[contains(@class, 'field_chairman')]//input"
    _BUTTON_CHAIRMAN_COMMITTEE = "//um-outlet//div[contains(text(), 'Председатель А. А.')]"

    _FIELD_CHOOSE_TK = "//span[label/mat-label[contains(text(), 'Выберите комиссию')]]/preceding-sibling::mat-select"
    _TK_DEMO_ONE = "//span//div[contains(text(), 'Демо коммисия 1')]"

    _FINAL_CONCLUSION = "Один победитель"
    _CHAIRMAN_COMMITTEE = "Председатель А. А."

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
            print(f"НЕт кнопки {e}")

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
        self.method_click(self._BUTTON_APPOINT_TK)

    @allure.step("Нажать кнопку 'Отмена'")
    def click_button_cencel(self):
        self.click_on_element(self._BUTTON_CENCEL)

    @allure.step("Выбрать коммисию ТК вручную")
    def choose_tk_(self):
        self.choose_chairman_committee()


    @allure.step("Выбрать коммисию ТК Демо коммисия 1")
    def choose_tk(self):
        time.sleep(1) #TODO
        self.method_click(self._FIELD_CHOOSE_TK)
        self.click_on_element(self._TK_DEMO_ONE)
        self.click_on_element(self._BUTTON_APPOINT_TK_DIALOG)
        self.click_on_element(self._BUTTON_STATEMENT)

    @allure.step("Выбрать Председателя коммиссии комиссии")
    def choose_chairman_committee(self):
        self.fill(self._FIELD_CHAIRMAN_COMMITTEE, self._CHAIRMAN_COMMITTEE)
        self.click_on_element(self._BUTTON_CHAIRMAN_COMMITTEE)

    @allure.step("Нажать кнопку 'Определить победителей'")
    def click_button_choose_winner(self):
        self.click_on_element(self._BUTTON_CHOOSE_WINNER)

    @allure.step("Выбор победителя 'Автоматически по общей сумме'")
    def choose_winner(self):
        self.click_on_element(self._FIELD_CHOOSE_WINNER)
        self.click_on_element(self._CHOOSE_WINNER)

    @allure.step("Заполнить 'Экспертное заключение'")
    def fill_final_conclusion(self):
        self.fill(self._FIELD_FINAL_CONCLUSION, self._FINAL_CONCLUSION)

    @allure.step("Нажать кнопку 'Сохранить и утвердить'")
    def click_button_save_and_approve(self):
        self.click_on_element(self._BUTTON_SAVE_AND_APPROVE)

    @allure.step("Нажать кнопку 'Утвердить результаты голосования'")
    def click_button_approve_results_vote(self):
        if self.wait_for_invisibility(self._BUTTON_APPROVE_RESULTS_VOTE):
            self.click_on_element(self._BUTTON_MENU)
            self.click_on_element(self._BUTTON_APPROVE_RESULTS_VOTE)
        else:
            self.click_on_element(self._BUTTON_APPROVE_RESULTS_VOTE)



    @allure.step("Нажать кнопку 'Утвердить протокол итогов этапа'")
    def click_button_approve_protocol_results(self):
        self.click_on_element(self._BUTTON_APPROVE_PROTOCOL_RESULTS)

    @allure.step("Нажать кнопку 'Утвердить'")
    def click_button_approve(self):
        self.click_on_element(self._BUTTON_APPROVE)


