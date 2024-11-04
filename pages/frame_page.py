import os.path
import time

import allure
from base.base_page import BasePage
from helpers.UI_helper import UIHelper
from data.links import Links
from data.credentials import Credentials


class FramePage(BasePage):
    _PAGE_URL = Links.FRAME_LINK

    _BUTTON_LOGIN_LOCATOR = '//span[text() = "Войти"]'
    _FIELD_LOGIN_LOCATOR = '//input[@formcontrolname="login"]'
    _FIELD_PASSWORD_LOCATOR = '//input[@formcontrolname="password"]'
    _BUTTON_NEXT_LOCATOR = '//button[@class="mat-focus-indicator self-center-um mat-primary mat-raised-button mat-button-base"]'

    @allure.step("Вводим логин и пароль организатора")
    def login_organizer(self):
        self.click_on_element(self._BUTTON_LOGIN_LOCATOR)
        self.fill(self._FIELD_LOGIN_LOCATOR, Credentials.LOGIN_ORGANIZER)
        self.fill(self._FIELD_PASSWORD_LOCATOR, Credentials.PASSWORD)
        self.click_on_element(self._BUTTON_NEXT_LOCATOR)

    @allure.step("Вводим логин и пароль первого участника")
    def login_participant_one(self):
        self.click_on_element(self._BUTTON_LOGIN_LOCATOR)
        self.fill(self._FIELD_LOGIN_LOCATOR, Credentials.LOGIN_PARTICIPANT_ONE)
        self.fill(self._FIELD_PASSWORD_LOCATOR, Credentials.PASSWORD)
        self.click_on_element(self._BUTTON_NEXT_LOCATOR)

    @allure.step("Вводим логин и пароль второго участника")
    def login_participant_two(self):
        self.click_on_element(self._BUTTON_LOGIN_LOCATOR)
        self.fill(self._FIELD_LOGIN_LOCATOR, Credentials.LOGIN_PARTICIPANT_TWO)
        self.fill(self._FIELD_PASSWORD_LOCATOR, Credentials.PASSWORD)
        self.click_on_element(self._BUTTON_NEXT_LOCATOR)



        # Метод с подгрузкой cookies #!TODO
        # if os.path.exists("cookies/login_cookies.pkl"):
        #     self.driver.delete_all_cookies()
        #     self.load_cookies("login_cookies")
        # else:
        #     self.click_on_element(self._BUTTON_LOGIN_LOCATOR)
        #     self.fill(self._FIELD_LOGIN_LOCATOR, self.credentials.LOGIN)
        #     self.fill(self._FIELD_PASSWORD_LOCATOR, self.credentials.PASSWORD)
        #     self.click_on_element(self._BUTTON_NEXT_LOCATOR)
        #     self.save_cookies("login_cookies")


