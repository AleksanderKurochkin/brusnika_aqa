from base.base_page import BasePage
from configs.data import DataUser



class MainPage(BasePage):

    _PAGE_URL = 'https://brusnika.demo.ultimeta.ru/frame/index.html'

    _BUTTON_LOGIN_LOCATOR = '//button[@class="mat-focus-indicator um-header-bar-trigger-btn mat-button mat-button-base mat-primary ng-star-inserted"]'
    _FIELD_LOGIN_LOCATOR = '//input[@formcontrolname="login"]'
    _FIELD_PASSWORD_LOCATOR = '//input[@formcontrolname="password"]'
    _BUTTON_NEXT_LOCATOR = '//button[@class="mat-focus-indicator self-center-um mat-primary mat-raised-button mat-button-base"]'
    _LOGO_USER = '//a[@id="user"]'

    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self):
        self.open_page()
        self.click_on_element(self._FIELD_LOGIN_LOCATOR)
        self.enter_text(self._FIELD_LOGIN_LOCATOR, DataUser.LOGIN_ORGANIZER_ONE_DEMO)
        self.enter_text(self._FIELD_PASSWORD_LOCATOR, DataUser.PASSWORD_DEMO_ORGANIZER_ONE)
        self.click_on_element(self._BUTTON_NEXT_LOCATOR)
