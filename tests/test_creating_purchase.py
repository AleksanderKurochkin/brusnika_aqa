import time

from base.base_test import BaseTest


class TestCreatingPurchase(BaseTest):
    def test_creating_purchase_request_proposals(self):
        self.main_page.login_user()
        self.trade_creation_page.creating_purchase_request_proposals()

        self.trade_creation_page.complete_form_purchase()
