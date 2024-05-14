import time

from base.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login_user(self):
        self.main_page.login_user()
        time.sleep(4)
        assert self.main_page.check()

