from base.base_page import BasePage
from pages.frame_page import FramePage
from pages.user_menu.my_profile_page import CardUserPage
from base.base_components.user_menu import UserMenu
from base.base_components.purchases import PurchasesMenu
from pages.create_purchase_page.create_purchase_good_tender import CreatePurchaseGoodTender
from pages.purchase_page.purchase_page_organizer import PurchasePageOrganizer
from pages.purchase_page.purchase_page_participant import PurchasePageParticipant
from pages.voting_page import VotingPages

class BaseTest:

    def setup_method(self):
        ## --Pages--
        self.base_page = BasePage(self.driver)
        self.frame_page = FramePage(self.driver)
        self.card_user_page = CardUserPage(self.driver)
        self.create_purchase_good_tender = CreatePurchaseGoodTender(self.driver)
        self.purchase_page_organizer = PurchasePageOrganizer(self.driver)
        self.purchase_page_participant = PurchasePageParticipant(self.driver)
        self.voting_page = VotingPages(self.driver)


        self.user_menu = UserMenu(self.driver)
        self.purchase = PurchasesMenu(self.driver)

