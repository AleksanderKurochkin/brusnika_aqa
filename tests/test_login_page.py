import allure
import pytest

from base.base_test import BaseTest


@allure.epic("Логин Пользователя")
class TestLoginPage(BaseTest):
    @pytest.mark.login
    @allure.title("Логин организатора")
    def test_login_organizer(self):
        self.frame_page.open()
        self.frame_page.login_organizer()





