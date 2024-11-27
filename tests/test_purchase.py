import time

from base.base_test import BaseTest
import allure

@allure.epic("Тест закупки МТР")
class TestPurchaseGood(BaseTest):

    @allure.title("Закупка ТМЦ: подача двух предложений с выбором победителя")
    def test_create_purchase(self):
        self.frame_page.open()
        self.frame_page.login_organizer()

        self.purchase.open_purchases_menu.open_new_purchase()
        self.purchase.purchase_good_tender()
        self.create_purchase_good_tender.create_purchase_good_tender()
        self.create_purchase_good_tender.click_approve_button()
        self.create_purchase_good_tender.click_without_invitation_button()
        self.create_purchase_good_tender.click_approve_and_declare_button()
        self.purchase_page_organizer.get_url_purchase()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_participant_one()

        self.purchase_page_participant.submit_offer()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_participant_two()

        self.purchase_page_participant.submit_offer()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_organizer()

        self.purchase_page_organizer.open_edit_purchase()
        self.create_purchase_good_tender.fill_edit_purchase()
        self.create_purchase_good_tender.fill_bid_submission_start_date()
        self.create_purchase_good_tender.fill_participation_confirmation_end_date_current()
        self.create_purchase_good_tender.fill_bid_submission_end_date_current()
        self.purchase_page_organizer.click_edit_purchase()
        self.purchase_page_organizer.click_button_result()
        self.purchase_page_organizer.click_button_appoint_tk()
        self.purchase_page_organizer.click_button_cencel()
        self.purchase_page_organizer.click_button_appoint_tk()
        self.purchase_page_organizer.choose_tk()

        self.purchase_page_organizer.click_button_choose_winner()
        self.purchase_page_organizer.choose_winner()
        self.purchase_page_organizer.fill_final_conclusion()
        self.purchase_page_organizer.click_button_save_and_approve()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_committee_member_one()

        self.voting_page.voting_committee_member()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_committee_member_two()

        self.voting_page.voting_committee_member()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_committee_chairman()

        self.voting_page.voting_committee_chairman()

        self.user_menu.open_user_menu.logout()
        self.purchase_page_organizer.open()
        self.frame_page.login_organizer()
        self.purchase_page_organizer.click_button_approve_results_vote()
        self.purchase_page_organizer.click_button_approve_protocol_results()
        self.purchase_page_organizer.click_button_approve()









