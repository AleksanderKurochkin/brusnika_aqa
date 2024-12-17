import time

from base.base_test import BaseTest
import pytest

class TestMenu(BaseTest):
    @pytest.mark.menu
    def test_open_menu(self):
        self.frame_page.open()
        self.frame_page.login_organizer()
        time.sleep(3)
        self.purchase.open_purchases_menu.open_new_purchase()
