import time

from base.base_page import BasePage
from locators.locators_trade_page import LocatorsTradePage
from configs.data import DataFormPurchase


class TradeCreationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def creating_purchase_request_proposals(self):  # ТМЦ
        self.click_on_element(LocatorsTradePage.BUTTON_NEW_PURCHASE_LOCATOR)
        self.click_on_element(LocatorsTradePage.BUTTON_PURCHASE_GOOD_TENDER_LOCATOR)

    def complete_form_purchase(self): # Заполнить форму закупки
        self.enter_text(LocatorsTradePage.FIELD_TITLE_LOCATOR, DataFormPurchase.TITLE)

        self.enter_text_and_click(LocatorsTradePage.FIELD_REGION_LOCATOR, DataFormPurchase.REGION, LocatorsTradePage.CHOOSE_REGION_LOCATOR)
        self.enter_text_and_click(LocatorsTradePage.FIELD_PURCHASE_CATEGORY_LOCATOR, DataFormPurchase.CATEGORY, LocatorsTradePage.CHOOSE_CATEGORY_LOCATOR)

        self.click_on_element(LocatorsTradePage.BUTTON_ADD_LOCATOR)
        time.sleep(5)



        # self.click_on_element(TradesPageLocators.BUTTON_SELECTION_PURCHASE)
        # self.click_on_element(TradesPageLocators.BUTTON_TEST_AQA_PURCHASE)
        # self.click_on_element(TradesPageLocators.BUTTON_SAVE_PURCHASE)
        # self.click_on_element(TradesPageLocators.BUTTON_ADD_STRING)
        # self.enter_text(TradesPageLocators.QUANTITY_FIELD, DataFormPurchase.QUANTITY)
        # self.click_on_element(TradesPageLocators.PRODUCT_NAME_FIELD)
