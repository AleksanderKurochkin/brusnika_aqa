from base.base_test import BaseTest
import pytest



class TestEditDataUser(BaseTest):
    @pytest.mark.edit_data_user
    def test_edit_second_name_user(self):
        self.frame_page.open()
        self.frame_page.login_organizer()
        self.user_menu.open_user_menu.open_my_profile_page()
        self.card_user_page.open_edit_page()
        self.card_user_page.rename_second_name()
        self.card_user_page.save_edit_page()




