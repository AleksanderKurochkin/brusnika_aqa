from datetime import datetime
from base.base_page import BasePage
import allure


class CreatePurchaseGoodTender(BasePage):
    # -- Field --
    _FIELD_TITLE = "//um-input-field[contains(@class, 'field_title ')]//input"
    _FIELD_REGION = "//um-combo-box-field[contains(@class, 'destinationRegion')]//input"
    _FIELD_PROCUREMENT_CATEGORY = "//um-combo-box-field[contains(@class, 'procurementClassifier')]//input"

    #--- Grid ---
    _FIELD_TITLE_POSITION = ("//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//td[@aria-colindex='2']//div["
                             "@class='mat-tooltip-trigger grid-cell__wrapper']")
    _INPUT_TITLE_POSITION = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//input[@role='combobox']"
    _FIELD_QUANTITY_POSITION = ("//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//td[@aria-colindex='4']//div["
                                "@class='mat-tooltip-trigger grid-cell__wrapper']")
    _INPUT_QUANTITY_POSITION = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//input[@tabindex='0']"
    _FIELD_ESTIMATED_GOOD_PRICE = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//td[@aria-colindex='6']//div[@class='mat-tooltip-trigger grid-cell__wrapper']"
    _INPUT_ESTIMATED_GOOD_PRICE = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//input[@tabindex='0']"
    _FIELD_SUBMISSION_FORM = "//um-select-field[contains(@class, 'submissionForm ')]// mat-select"
    _FIELD_PURCHASE_TERMS = "//um-combo-box-field[contains(@class, 'purchaseTerms ')]//input"
    _FIELD_PAYMENT_TERMS_TYPE = "//um-select-field[contains(@class, 'paymentTermsType ')]//mat-select"
    _FIELD_EDIT_PURCHASE = "//um-textarea-field[contains(@class, 'field_modificationReason')]//textarea"
    _BUTTON_ADD = "//kendo-grid[@class='virtual-scroll k-grid k-grid-virtual']//span[text()='Добавить']"

    _LOCATOR_REGION = "//span[contains(text(), 'Москва')]"
    _LOCATOR_PROCUREMENT_CATEGORY = "//span[contains(text(), 'Procurement')]"
    _LOCATOR_TITLE_POSITION = "//span[contains(text(), 'Вентилятор')]"
    _SUBMISSION_FORM = "//span[@class='mat-option-text']//div[contains(text(), 'Не показывать участникам сведения о других предложениях (закрытая форма подачи предложений о цене)')]"
    _PURCHASE_TERMS = "//span[contains(text(), 'DAP-')]"
    _PAYMENT_TERMS_TYPE = "//div[@role='listbox']//div[contains(text(), 'Единовременный аванс')]"

    _PARTICIPATION_CONFIRMATION_END_DATE = "//um-date-time-field[contains(@class, 'field_participationConfirmationEndDate')]//input[@formcontrolname='date']"
    _PARTICIPATION_CONFIRMATION_END_DATE_TIME = "//um-date-time-field[contains(@class, 'field_participationConfirmationEndDate')]//input[@formcontrolname='time']"
    _BID_SUBMISSION_END_DATE = "//um-date-time-field[contains(@class, 'field_bidSubmissionEndDate ')]//input[@formcontrolname='date']"
    _BID_SUBMISSION_END_DATE_TIME = "//um-date-time-field[contains(@class, 'field_bidSubmissionEndDate ')]//input[@formcontrolname='time']"
    _BID_SUBMISSION_START_DATE = "//um-date-time-field[contains(@class, 'field_bidSubmissionStartDate')]//input[@formcontrolname='date']"
    _BID_SUBMISSION_START_TIME = "//um-date-time-field[contains(@class, 'field_bidSubmissionStartDate')]//input[@formcontrolname='time']"

    #--DATA
    _TITLE = f"AQA_Закупка_ТМЦ {datetime.now().strftime('%d.%m.%Y')} {datetime.now().strftime('%H:%M')}"
    _REGION = "Москва"
    _PROCUREMENT_CATEGORY = "Procurement"
    _TITLE_POSITION = "Вентилятор"
    _QUANTITY_POSITION = "100"
    _ESTIMATED_GOOD_PRICE = "2000"

    #--Кнопки
    _BUTTON_APPROVE = "//mat-toolbar-row[contains(@class, 'star-inserted')]//a[contains(@class, 'mat-flat-button')]"
    _BUTTON_CONTINUE_WITHOUT_INVITATION = "//span[contains(text(), 'Продолжить без приглашения')]"
    _BUTTON_APPROVE_AND_DECLARE = "//span[contains(text(), 'Утвердить и объявить')]"
    _EDIT_PURCHASE = "Изменение времени"

    @allure.step("Заполняем 'Наименование (предмет закупки)'")
    def fill_title(self):
        self.fill(self._FIELD_TITLE, self._TITLE)

    @allure.step("Заполняем 'Регион'")
    def fill_region(self):
        self.fill(self._FIELD_REGION, self._REGION)
        self.find(self._LOCATOR_REGION).click()

    @allure.step("Заполняем 'Категорию закупки'")
    def fill_procurement_category(self):
        self.fill(self._FIELD_PROCUREMENT_CATEGORY, self._PROCUREMENT_CATEGORY)
        self.find(self._LOCATOR_PROCUREMENT_CATEGORY).click()

    @allure.step("Добавление строки в 'Спецификацию поставки'")
    def add_string_delivery_specification(self):
        self.find(self._BUTTON_ADD).click()

    @allure.step("Заполнение строки в 'Спецификацию поставки'")
    def add_position_delivery_specification(self):
        self.find(self._FIELD_TITLE_POSITION).click()
        self.fill(self._INPUT_TITLE_POSITION, self._TITLE_POSITION)
        self.find(self._LOCATOR_TITLE_POSITION).click()
        self.find(self._FIELD_QUANTITY_POSITION).click()
        self.fill(self._INPUT_QUANTITY_POSITION, self._QUANTITY_POSITION)
        self.find(self._FIELD_ESTIMATED_GOOD_PRICE).click()
        self.fill(self._INPUT_ESTIMATED_GOOD_PRICE, self._ESTIMATED_GOOD_PRICE)

    @allure.step("Заполнение 'Форма подачи предложений о цене*'")
    def fill_submission_form(self):
        self.find(self._FIELD_SUBMISSION_FORM).click()
        self.find(self._SUBMISSION_FORM).click()

    @allure.step("Заполнение 'условия поставки'")
    def fill_purchase_terms(self):
        self.find(self._FIELD_PURCHASE_TERMS).click()
        self.find(self._PURCHASE_TERMS).click()

    @allure.step("Заполнение 'Условия оплаты'")
    def fill_pyment_terms_type(self):
        self.find(self._FIELD_PAYMENT_TERMS_TYPE).click()
        self.find(self._PAYMENT_TERMS_TYPE).click()

    @allure.step("Заполнить 'Окончание подтверждения участия' +3 мин")
    def fill_participation_confirmation_end_date(self):
        self.fill_date_ant_time_plus_3_min(self._PARTICIPATION_CONFIRMATION_END_DATE, self._PARTICIPATION_CONFIRMATION_END_DATE_TIME)

    @allure.step("Заполнить 'Окончание представления предложений +3 мин'")
    def fill_bid_submission_end_date(self):
        self.fill_date_ant_time_plus_3_min(self._BID_SUBMISSION_END_DATE, self._BID_SUBMISSION_END_DATE_TIME)

    @allure.step("Заполнить 'Окончание подтверждения участия' тек. дата")
    def fill_participation_confirmation_end_date_current(self):
        self.fill_date_ant_time_current(self._PARTICIPATION_CONFIRMATION_END_DATE,
                                           self._PARTICIPATION_CONFIRMATION_END_DATE_TIME)

    @allure.step("Заполнить 'Окончание представления предложений тек. дата'")
    def fill_bid_submission_end_date_current(self):
        self.fill_date_ant_time_current(self._BID_SUBMISSION_END_DATE, self._BID_SUBMISSION_END_DATE_TIME)

    @allure.step("Заполнить 'Начало представления предложений - 1 мин'")
    def fill_bid_submission_start_date(self):
        self.fill_date_ant_time_minus_1_min(self._BID_SUBMISSION_START_DATE, self._BID_SUBMISSION_START_TIME)

    @allure.step("Нажать кнопку 'Посмотреть и утвердить'")
    def click_approve_button(self):
        self.find(self._BUTTON_APPROVE).click()

    @allure.step("Нажать кнопку в диалоговом окне 'Продолжить без приглашения'")
    def click_without_invitation_button(self):
        self.find(self._BUTTON_CONTINUE_WITHOUT_INVITATION).click()

    @allure.step("Нажать кнопку 'Утвердить и объявить'")
    def click_approve_and_declare_button(self):
        self.find(self._BUTTON_APPROVE_AND_DECLARE).click()

    @allure.step("Заполнить Обоснование внесения изменений")
    def fill_edit_purchase(self):
        self.fill(self._FIELD_EDIT_PURCHASE, self._EDIT_PURCHASE)

    @allure.step("Создать закупку ТМЦ")
    def create_purchase_good_tender(self):
        self.fill_title()
        self.fill_region()
        self.fill_procurement_category()
        self.add_string_delivery_specification()
        self.add_position_delivery_specification()
        self.fill_submission_form()
        self.fill_purchase_terms()
        self.fill_pyment_terms_type()
        self.fill_participation_confirmation_end_date()
        self.fill_bid_submission_end_date()























