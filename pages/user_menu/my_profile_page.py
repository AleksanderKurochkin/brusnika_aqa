import allure
from data.links import Links
from base.base_page import BasePage


class CardUserPage(BasePage):
    _PAGE_URL = Links.PROFILE_LINK

    _EDIT_BUTTON_LOCATOR = '//span[text()="Изменить"]'

    _SAVE_EDIT_BUTTON = '//a[@tabindex="0"]//span[text() = "Сохранить изменения"]'
    _FIELD_SECOND_NAME_LOCATOR = '//div//input[@id="mat-input-4"]'
    _NEW_SECOND_NAME = 'Петров'

    @allure.step("Нажать кнопку изменить на странице профиля")
    def open_edit_page(self):
        self.click_on_element(self._EDIT_BUTTON_LOCATOR)

    @allure.step("Ввести новую фамилию")
    def rename_second_name(self):
        self.fill(self._FIELD_SECOND_NAME_LOCATOR, self._NEW_SECOND_NAME)

    @allure.step("Сохранить изменения")
    def save_edit_page(self):
        self.click_on_element(self._SAVE_EDIT_BUTTON)
