from helpers.UI_helper import UIHelper
import time
import allure
from metaclasses.meta_lokators import MetaLocator


class PurchasesMenu(UIHelper, metaclass=MetaLocator):


    _PURCHASES = "//um-navigation-item[.//span[text()='Закупки']]"

    _NEW_PURCHASES = "//span[text() = 'Новая закупка']"
    _GOOD_TENDER = '//div[@class="modal-content"]//span[text() = "Тендер на закупку ТМЦ"]'
    _WORK_TENDER = '//div[@class ="modal-content"]//span[text() = "Тендер на оказание работ, услуг"]'

    @property
    def open_purchases_menu(self):
        if 'open' not in self.find(self._PURCHASES).get_attribute('class'):
            self.click_on_element(self._PURCHASES)
        else:
            pass
        return self

    @allure.step("Открыть Новая закупка")
    def open_new_purchase(self):
        self.click_on_element(self._NEW_PURCHASES)
        time.sleep(2)  # !TODO


    @allure.step("Выбрать закупку ТМЦ")
    def purchase_good_tender(self):
        self.click_on_element(self._GOOD_TENDER)
        time.sleep(2) # !TODO


    @allure.step("Выбрать закупку СМР")
    def purchase_work_tender(self):
        self.click_on_element(self._WORK_TENDER)
