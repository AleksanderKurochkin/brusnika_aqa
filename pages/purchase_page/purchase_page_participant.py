import os
from base.base_page import BasePage
import allure
import time

class PurchasePageParticipant(BasePage):

    _BUTTON_SUBMIT_OFFER = "//span[contains(text(), 'Подать предложение')]"
    _BUTTON_CONFIRMATION_PARTICIPATION = "//span[contains(text(), 'Подтвердить участие')]"

    _BUTTON_SUBMIT_OFFER_CONFIRMATION = "//div[contains(@id, 'cdk-overlay')]//span[contains(text(), 'Подать предложение')]"

    _FIELD_SUPPLER_STATE = "//mat-select[following-sibling::span//label//mat-label[text()='Статус поставщика']]"

    _FIELD_PRICE = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//td[@aria-colindex='6']//div[@class='mat-tooltip-trigger grid-cell__wrapper']"
    _INPUT_PRICE = "//kendo-grid-list//tr[@data-kendo-grid-item-index='0']//input[@tabindex='0']"
    _FIELD_PREPAYMENT_PERCENT = "//input[@id=(//mat-label[contains(text(), 'Размер аванса')]/ancestor::label/@for)]"

    _INPUT_COMMERCIAL_OFFER_ATTACHMENTS = "//um-file-field[contains(@class, 'field_commercialOfferAttachments')]//input[@type='file']"
    _NAME_FILE = "Specification.xlsx"

    _PRICE = "2500"
    _SUPPLER_STATE = "//div[@role='listbox']//div[contains(text(), 'Дилер производителя')]"
    _PREPAYMENT_PERCENT = "30"

    @allure.step("Нажать на кнопку  Подтвердить участие")
    def click_button_confirm_participation(self):
        self.click_on_element(self._BUTTON_CONFIRMATION_PARTICIPATION)



    @allure.step("Нажать на кнопку  Подать предложение")
    def click_button_sabmit_offer(self):
        self.click_on_element(self._BUTTON_SUBMIT_OFFER)

    @allure.step("Ввести стоимость")
    def fill_price(self):
        self.find(self._FIELD_PRICE).click()
        self.fill(self._INPUT_PRICE, self._PRICE)


    @allure.step("Выбрать статус поставщика")
    def choice_suppler_state(self):
        self.click_on_element(self._FIELD_SUPPLER_STATE)
        self.click_on_element(self._SUPPLER_STATE)

    @allure.step("Заполнить Условия оплаты (Аванс)")
    def fill_prepayment_percent(self):
        self.fill(self._FIELD_PREPAYMENT_PERCENT, self._PREPAYMENT_PERCENT)

    @allure.step("Загрузка 'Коммерческого предложения'")
    def load_commercial_offer_attachments(self):
        self.load_file(self._INPUT_COMMERCIAL_OFFER_ATTACHMENTS, self._NAME_FILE)

    @allure.step("Нажать на кнопку  Подать предложение. Подтверждение")
    def click_button_sabmit_offer_confirmation(self):
        self.click_on_element(self._BUTTON_SUBMIT_OFFER_CONFIRMATION)

    @allure.step("Заполнить Обоснование внесения изменений")
    def fill_edit_purchase(self):
        self.fill(self._FIELD_EDIT_PURCHASE, self._EDIT_PURCHASE)


    @allure.step("Подать предложение")
    def submit_offer(self):
        self.click_button_confirm_participation()
        self.click_button_yes()
        self.click_button_sabmit_offer()
        self.fill_price()
        self.choice_suppler_state()
        self.fill_prepayment_percent()
        self.load_commercial_offer_attachments()
        time.sleep(5)  # TODO
        self.click_button_sabmit_offer()
        self.click_button_sabmit_offer_confirmation()





