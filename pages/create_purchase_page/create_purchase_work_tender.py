from datetime import datetime
from base.base_page import BasePage
import allure


class CreatePurchaseWorkTender(BasePage):
    # -- Field --
    _FIELD_TITLE = "//input[@id=(//mat-label[contains(text(), 'Наименование (предмет закупки)')]/ancestor::label/@for)]"
    _FIELD_REGION = "//um-combo-box-field[contains(@class, 'destinationRegion')]//input"
    _FIELD_PROCUREMENT_CATEGORY = "//um-combo-box-field[contains(@class, 'procurementClassifier')]//input"
    _FIELD_EXECUTION_PERIOD = "//um-textarea-field[contains(@class, 'executionPeriod')]//textarea"
    _FIELD_GUARANTEE_PERIOD_RESERVE_ASSURANCE = "//um-textarea-field[contains(@class, 'guaranteePeriodReserveAssurance')]//textarea"
    _FIELD_GENERAL_CONTRACTION_PERCENTAGE = "//um-input-field[contains(@class, 'generalContractingPercentage')]//input"
    _FIELD_GUARANTEE_PERIOD = "//um-textarea-field[contains(@class, 'guaranteePeriod ')]//textarea"

    _LOCATOR_REGION = "//span[contains(text(), 'Москва')]"
    _LOCATOR_PROCUREMENT_CATEGORY = "//span[contains(text(), 'Procurement')]"

    #--- Toggler ---
    _TOGGLER_ENABLE_PRICE_PER_PURCHASE_ITEM_CHECKBOX = "//um-checkbox-field[contains(@class,'field_enablePricePerPurchaseItem')]//input"
    _TOGGLER_ENABLE_PRICE_PER_PURCHASE_ITEM_BUTTON = "//um-checkbox-field[contains(@class, 'field_enablePricePerPurchaseItem')]//span[@class='mat-slide-toggle-content']"
    _TOGGLER_ALLOW_PAYMENTS_STAGE_IN_BID_CHECKBOX = "//um-checkbox-field[contains(@class,'allowPaymentStagesInBid')]//input"
    _TOGGLER_ALLOW_PAYMENTS_STAGE_IN_BID_BUTTON = "//um-checkbox-field[contains(@class, 'allowPaymentStagesInBid')]//span[@class='mat-slide-toggle-content']"
    _TOGGLER_PAYMENT_STAGE_PERIOD_IN_STAGE_CHECKBOX = "//um-checkbox-field[contains(@class,'paymentStagesPeriodInTrade')]//input"
    _TOGGLER_PAYMENT_STAGE_PERIOD_IN_STAGE_BUTTON = "//um-checkbox-field[contains(@class, 'paymentStagesPeriodInTrade')]//span[@class='mat-slide-toggle-content']"
    _TOGGLER_PAYMENT_STAGE_PERCENTS_IN_TRADE_CHECKBOX = "//um-checkbox-field[contains(@class,'paymentStagesPercentsInTrade')]//input"
    _TOGGLER_PAYMENT_STAGE_PERCENTS_IN_TRADE_BUTTON = "//um-checkbox-field[contains(@class, 'paymentStagesPercentsInTrade')]//span[@class='mat-slide-toggle-content']"

    ##--- Payment Stage---
    _BUTTON_ADD_PAYMENT_STAGE = "//um-grid-field[contains(@class, 'paymentStages')]//span[text() = 'Добавить']"
    _TYPE = "//um-grid-field[contains(@class, 'paymentStages')]//tr[@data-kendo-grid-item-index = '0']//um-select-field-preview[contains(@class, 'type')]/ancestor::div[2]"
    _CHOICE_TYPE = "//um-grid-field[contains(@class, 'paymentStages')]//mat-select[contains(@class, 'mat-select mat-tooltip-trigger')]//span"
    _TYPE_END_WORKS = "//mat-option//div[contains(text(), 'По факту выполнения работ')]"
    # class ="mat-select-arrow-wrapper    //um-grid-field[contains(@class, 'paymentStages')]//tr[@data-kendo-grid-item-index = '0']//mat-form-field   //um-grid-field[contains(@class, 'paymentStages')]//tr[@data-kendo-grid-item-index = '0']//um-select-field
    _PERCENTS = "//um-grid-field[contains(@class, 'paymentStages')]//tr[@data-kendo-grid-item-index = '0']//um-number-field-preview[contains(@class, 'percents')]/ancestor::div[2]"
    _CHOICE_PERCENTS = "100"
    _PAYMENT_FORM = "//um-grid-field[contains(@class, 'paymentStages')]//tr[@data-kendo-grid-item-index = '0']//um-select-field-preview[contains(@class, 'paymentForm ')]/ancestor::div[2]"
    _CHOICE_PAYMENT_FORM = "//um-grid-field[contains(@class, 'paymentStages')]//mat-select[contains(@class, 'mat-select mat-tooltip-trigger')]//span"
    _MONEY = "//mat-option//div[contains(text(), 'Деньги')]"

    #--- DATA ---
    _TITLE = f"AQA_Закупка_СМР {datetime.now().strftime('%d.%m.%Y')} {datetime.now().strftime('%H:%M')}"
    _REGION = "Москва"
    _PROCUREMENT_CATEGORY = "Procurement"
    _EXECUTION_PERIOD = "120"
    _GUARANTEE_PERIOD_RESERVE_ASSURANCE = "банковская гарантия"
    _GENERAL_CONTRACTION_PERCENTAGE = "5%"
    _GUARANTEE_PERIOD = "2 года"

    #--- Button ---
    _BUTTON_APPROVE = "//mat-toolbar-row[contains(@class, 'star-inserted')]//a[contains(@class, 'mat-flat-button')]"
    _BUTTON_CONTINUE_WITHOUT_INVITATION = "//span[contains(text(), 'Продолжить без приглашения')]"
    _BUTTON_APPROVE_AND_DECLARE = "//span[contains(text(), 'Утвердить и объявить')]"
    _EDIT_PURCHASE = "Изменение времени"

    #--Date and time--
    _PARTICIPATION_CONFIRMATION_END_DATE = "//um-date-time-field[contains(@class, 'field_participationConfirmationEndDate')]//input[@formcontrolname='date']"
    _PARTICIPATION_CONFIRMATION_END_DATE_TIME = "//um-date-time-field[contains(@class, 'field_participationConfirmationEndDate')]//input[@formcontrolname='time']"
    _BID_SUBMISSION_END_DATE = "//um-date-time-field[contains(@class, 'field_bidSubmissionEndDate ')]//input[@formcontrolname='date']"
    _BID_SUBMISSION_END_DATE_TIME = "//um-date-time-field[contains(@class, 'field_bidSubmissionEndDate ')]//input[@formcontrolname='time']"
    _BID_SUBMISSION_START_DATE = "//um-date-time-field[contains(@class, 'field_bidSubmissionStartDate')]//input[@formcontrolname='date']"
    _BID_SUBMISSION_START_TIME = "//um-date-time-field[contains(@class, 'field_bidSubmissionStartDate')]//input[@formcontrolname='time']"
    #--- Input ---
    _INPUT_PURCHASE_ITEM_ATTACHMENTS = "//um-grid-field[contains(@class, 'field_purchaseItems')]//um-excel-import//input[@type='file']"
    _NAME_FILE = "Ведомость работ и материалов к лоту (2).xlsx"

    @allure.step(f"Заполняем 'Наименование (предмет закупки){_TITLE}'")
    def fill_title(self):
        self.fill(self._FIELD_TITLE, self._TITLE)

    @allure.step(f"Заполняем 'Регион'{_REGION}")
    def fill_region(self):
        self.fill(self._FIELD_REGION, self._REGION)
        self.find(self._LOCATOR_REGION).click()

    @allure.step(f"Заполняем 'Общий срок выполнения работ {_EXECUTION_PERIOD}'")
    def fill_execution_period(self):
        self.fill(self._FIELD_EXECUTION_PERIOD, self._EXECUTION_PERIOD)

    @allure.step("Включить Указать расчетную стоимость")
    def toggler_enable_price_per_purchase_item_on(self):
        self.toggler(self._TOGGLER_ENABLE_PRICE_PER_PURCHASE_ITEM_CHECKBOX,
                     self._TOGGLER_ENABLE_PRICE_PER_PURCHASE_ITEM_BUTTON, flag="on")

    @allure.step("Загрузка 'Спецификации поставки'")
    def load_purchase_item(self):
        self.load_file(self._INPUT_PURCHASE_ITEM_ATTACHMENTS, self._NAME_FILE)

    @allure.step(f"Заполняем 'Категорию закупки' {_PROCUREMENT_CATEGORY}")
    def fill_procurement_category(self):
        self.fill(self._FIELD_PROCUREMENT_CATEGORY, self._PROCUREMENT_CATEGORY)
        self.find(self._LOCATOR_PROCUREMENT_CATEGORY).click()

    @allure.step(f"Заполняем 'Обеспечение суммы резерва качества на гарантийный срок после подписания итогового акта {_GUARANTEE_PERIOD_RESERVE_ASSURANCE}'")
    def fill_guarantee_period_reserve_assurance(self):
        self.fill(self._FIELD_GUARANTEE_PERIOD_RESERVE_ASSURANCE, self._GUARANTEE_PERIOD_RESERVE_ASSURANCE)

    @allure.step(f"Заполняем 'Генподрядный процент' {_GENERAL_CONTRACTION_PERCENTAGE}")
    def fill_general_contracting_percentage(self):
        self.fill(self._FIELD_GENERAL_CONTRACTION_PERCENTAGE, self._GENERAL_CONTRACTION_PERCENTAGE)

    @allure.step("Выключить 'Поставщик может предложить свои условия оплаты'")
    def toggler_allow_payment_stages_in_bid_off(self):
        self.toggler(self._TOGGLER_ALLOW_PAYMENTS_STAGE_IN_BID_CHECKBOX,
                     self._TOGGLER_ALLOW_PAYMENTS_STAGE_IN_BID_BUTTON, flag="off")

    @allure.step("Включить 'Задать сроки выплат'")
    def toggler_payment_stages_period_in_trade_off(self):
        self.toggler(self._TOGGLER_PAYMENT_STAGE_PERIOD_IN_STAGE_CHECKBOX,
                     self._TOGGLER_PAYMENT_STAGE_PERIOD_IN_STAGE_BUTTON, flag="off")

    @allure.step("Включить 'Задать суммы выплат'")
    def toggler_payment_stages_percents_in_trade_off(self):
        self.toggler(self._TOGGLER_PAYMENT_STAGE_PERCENTS_IN_TRADE_CHECKBOX,
                     self._TOGGLER_PAYMENT_STAGE_PERCENTS_IN_TRADE_BUTTON, flag="off")

    @allure.step("Добавить строку условий выплат")
    def add_string_payment_stage(self):
        self.click_on_element(self._BUTTON_ADD_PAYMENT_STAGE)

    @allure.step(f"Заполнить тип выплаты {_TYPE_END_WORKS}")
    def add_type_payment_stage(self):
        self.click_on_element(self._TYPE)
        self.click_on_element(self._CHOICE_TYPE)
        self.click_on_element(self._TYPE_END_WORKS)

    @allure.step(f"Заполнить поценты {_CHOICE_PERCENTS}")
    def add_percent_payment_stage(self):
        self.fill(self._PERCENTS, self._CHOICE_PERCENTS)

    @allure.step(f"Заполнить форму выплат {_MONEY}")
    def add_form_payment_stage(self):
        self.click_on_element(self._PAYMENT_FORM)
        self.click_on_element(self._MONEY)

    @allure.step(f"Заполнить гарантийный период {_GUARANTEE_PERIOD}")
    def fill_guarantee_period(self):
        self.fill(self._FIELD_GUARANTEE_PERIOD, self._GUARANTEE_PERIOD)

    @allure.step("Заполнить 'Окончание подтверждения участия' +3 мин")
    def fill_participation_confirmation_end_date(self):
        self.fill_date_ant_time_plus_3_min(self._PARTICIPATION_CONFIRMATION_END_DATE, self._PARTICIPATION_CONFIRMATION_END_DATE_TIME)

    @allure.step("Заполнить 'Окончание представления предложений +3 мин'")
    def fill_bid_submission_end_date(self):
        self.fill_date_ant_time_plus_3_min(self._BID_SUBMISSION_END_DATE, self._BID_SUBMISSION_END_DATE_TIME)

    # @allure.step("Заполнить 'Окончание подтверждения участия' тек. дата")
    # def fill_participation_confirmation_end_date_current(self):
    #     self.fill_date_ant_time_current(self._PARTICIPATION_CONFIRMATION_END_DATE,
    #                                        self._PARTICIPATION_CONFIRMATION_END_DATE_TIME)
    #
    # @allure.step("Заполнить 'Окончание представления предложений тек. дата'")
    # def fill_bid_submission_end_date_current(self):
    #     self.fill_date_ant_time_current(self._BID_SUBMISSION_END_DATE, self._BID_SUBMISSION_END_DATE_TIME)
    #
    # @allure.step("Заполнить 'Начало представления предложений - 1 мин'")
    # def fill_bid_submission_start_date(self):
    #     self.fill_date_ant_time_minus_1_min(self._BID_SUBMISSION_START_DATE, self._BID_SUBMISSION_START_TIME)

    @allure.step("Нажать кнопку 'Сохранить и продолжить'")
    def click_approve_button(self):
        self.click_on_element(self._BUTTON_APPROVE)

    @allure.step("Нажать кнопку в диалоговом окне 'Продолжить без приглашения'")
    def click_without_invitation_button(self):
        self.click_on_element(self._BUTTON_CONTINUE_WITHOUT_INVITATION)

    @allure.step("Нажать кнопку 'Утвердить и объявить'")
    def click_approve_and_declare_button(self):
        self.click_on_element(self._BUTTON_APPROVE_AND_DECLARE)

    # @allure.step("Заполнить Обоснование внесения изменений")
    # def fill_edit_purchase(self):
    #     self.fill(self._FIELD_EDIT_PURCHASE, self._EDIT_PURCHASE)

    @allure.step("заполнить условия оплаты: по факту выполненных работ")
    def choice_payment_stage(self):
        self.add_string_payment_stage()
        self.add_type_payment_stage()
        self.add_form_payment_stage()

    @allure.step("Создать закупку СМР")
    def create_purchase_work_tender(self):
        self.fill_title()
        self.fill_region()
        self.fill_procurement_category()
        self.fill_execution_period()
        self.toggler_enable_price_per_purchase_item_on()
        self.load_purchase_item()
        self.fill_guarantee_period_reserve_assurance()
        self.fill_general_contracting_percentage()
        self.toggler_allow_payment_stages_in_bid_off()
        self.toggler_payment_stages_period_in_trade_off()
        self.toggler_payment_stages_percents_in_trade_off()
        self.choice_payment_stage()
        self.fill_guarantee_period()
        self.fill_participation_confirmation_end_date()
        self.fill_bid_submission_end_date()
        self.click_approve_button()
        self.click_without_invitation_button()
        self.click_approve_and_declare_button()