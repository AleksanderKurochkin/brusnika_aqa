import time

import pytest
from base.base_test import BaseTest
import allure

@allure.epic("Тест создания закупок СМР")
class TestPurchaseWork(BaseTest):
    @pytest.mark.purchas_work_tender
    @allure.title("Закупка СМР: создание закупки с подгрузкой ведомости через UI")
    def test_create_purchase_work_tender(self):
        self.frame_page.open()
        self.frame_page.login_organizer()
        self.purchase.open_purchases_menu.open_new_purchase()
        self.purchase.purchase_work_tender()
        self.create_purchase_work_tender.create_purchase_work_tender()

    @pytest.mark.purchas_work_tender_soap
    @allure.title("Закупка СМР: создание закупки через SOAP")
    def test_create_purchase_work_tender_soap(self):
        self.soap_requests.upload_works_tender_request()
        self.soap_requests.get_url_purchase()
        self.soap_requests.open()
        self.frame_page.login_organizer()





