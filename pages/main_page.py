from base.base_page import BasePage
from configs.links import Links
from configs.data import DataUser
from locators.locators_main_page import LocatorsMainPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self):
        self.open_page(Links.MAIN_PAGE)
        self.click_on_element(LocatorsMainPage.BUTTON_LOGIN)
        self.enter_text(LocatorsMainPage.FIELD_LOGIN, DataUser.LOGIN_DEMO_ORGANIZER_ONE)
        self.enter_text(LocatorsMainPage.FIELD_PASSWORD, DataUser.PASSWORD_DEMO_ORGANIZER_ONE)
        self.click_on_element(LocatorsMainPage.BUTTON_NEXT)
