from helpers.UI_helper import UIHelper
import time
import allure
from metaclasses.meta_lokators import MetaLocator


class UserMenu(UIHelper, metaclass=MetaLocator):

    _USER_MENU_LOCATOR = '//a[@id = "user"]'

    _MY_PROFILE = '//div[@class="cdk-overlay-pane"]//span[text()="Мой профиль"]'
    _MY_ORGANIZATION = '//div[@class="cdk-overlay-pane"]//span[text()="Моя организация"]'
    _MY_MAILING = '//div[@class="cdk-overlay-pane"]//span[text()="Мои рассылки"]'
    _LOGOUT = '//div[@class="cdk-overlay-pane"]//span[text()="Выйти"]'

    @property
    def open_user_menu(self):
        self.click_on_element(self._USER_MENU_LOCATOR)
        return self

    @allure.step("Открыть Мой профиль")
    def open_my_profile_page(self):
        time.sleep(3) #! TODO
        self.click_on_element(self._MY_PROFILE)

    @allure.step("Открыть Моя организация")
    def open_my_organization_page(self):
        time.sleep(3)  # ! TODO
        self.click_on_element(self._MY_ORGANIZATION)

    @allure.step("Открыть Мои рассылки")
    def open_my_mailing_page(self):
        time.sleep(3)  # ! TODO
        self.click_on_element(self._MY_MAILING)

    @allure.step("Разлогинится Выход")
    def logout(self):
        time.sleep(3)  # ! TODO
        self.click_on_element(self._LOGOUT)