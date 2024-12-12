from metaclasses.meta_lokators import MetaLocator
from base.base_components.user_menu import UserMenu
from helpers.UI_helper import UIHelper
import allure
import time


class BasePage(UIHelper, metaclass=MetaLocator):

    _BUTTON_YES = "//span[text() = 'Да']"


    @allure.step("Нажать на кнопку  да")
    def click_button_yes(self):
        self.click_on_element(self._BUTTON_YES)

    ## --- Вкл/ Выкл тоглер через флаг ---
    def toggler(self, locator_checkbox, locator_button, flag="on"):
        if flag == "on":
            self.toggle_on(locator_checkbox, locator_button)
        elif flag == "off":
            self.toggle_off(locator_checkbox, locator_button)






