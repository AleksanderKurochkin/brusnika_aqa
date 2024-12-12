import time
import pytest
from base.base_test import BaseTest
import allure

@allure.epic("Тест закупок СМР")
class TestPurchaseGood(BaseTest):
    @pytest.mark.purchas_work_tender
    @allure.title("Закупка СМР: два лота, один отмена по второму выбран победитель")
    def test_create_purchase(self):
        self.frame_page.open()
        self.frame_page.login_organizer()

        self.purchase.open_purchases_menu.open_new_purchase()
        self.purchase.purchase_work_tender()
        self.create_purchase_work_tender.create_purchase_work_tender()


        time.sleep(5)