import time

import allure
from base.base_page import BasePage

class VotingPages(BasePage):

    _BUTTON_VOTE = "//mat-toolbar//span[contains(text(), 'Голосование')]"
    _BUTTON_ZA = "//mat-button-toggle-group//mat-button-toggle[@value='AGREE']//button"
    _BUTTON_VOTING = "//button[.//span[contains(text(), 'Проголосовать')]]"

    @allure.step("Нажать кнопку 'Голосование'")
    def __click_button_vote(self):
        self.click_on_element(self._BUTTON_VOTE)

    @allure.step("Нажать кнопку 'За'")
    def __click_button_za(self):
        self.click_on_element(self._BUTTON_ZA)

    @allure.step("Нажать кнопку 'Проголосовать'")
    def __click_button_voting(self):
        self.click_on_element(self._BUTTON_VOTING)

    @allure.step("Голосование члена комиссии")
    def voting_committee_member(self):
        self.__click_button_vote()
        self.__click_button_za()
        self.__click_button_voting()

    @allure.step("Голосование председателя комиссии")
    def voting_committee_chairman(self):
        self.__click_button_vote()
        self.__click_button_za()
        self.__click_button_voting()
