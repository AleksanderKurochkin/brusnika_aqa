import pytest
from base.base_test import BaseTest
import allure

@allure.epic("Тест создания закупок СМР")
class TestPurchaseWork(BaseTest):
    @pytest.mark.purchas_work_tender
    @allure.title("Закупка СМР: создание закупки через UI")
    def test_create_purchase_work_tender(self):
        self.frame_page.open()
        self.frame_page.login_organizer()
        self.purchase.open_purchases_menu.open_new_purchase()
        self.purchase.purchase_work_tender()
        self.create_purchase_work_tender.create_purchase_work_tender()

    @pytest.mark.purchas_work_tender_soap
    @allure.title("Закупка СМР: создание черновика закупки через SOAP + создание закупки")
    def test_create_purchase_work_tender_soap(self):
        self.soap_requests.upload_works_tender_request()
        self.soap_requests.get_url_purchase()
        self.soap_requests.open()
        self.frame_page.login_organizer()
        self.purchase_page_organizer.open_edit_purchase()
        self.create_purchase_work_tender.fill_region()
        self.create_purchase_work_tender.fill_bid_submission_end_date()
        self.create_purchase_work_tender.fill_participation_confirmation_end_date()
        self.create_purchase_work_tender.click_save_and_continue_button()





