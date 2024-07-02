class LocatorsTradePage:
    BUTTON_NEW_PURCHASE_LOCATOR = ('xpath', '//div[@class="layout-vertical-um nav-bar-container"]//span[text()="Новая закупка"]')
    BUTTON_PURCHASE_GOOD_TENDER_LOCATOR = ('xpath', "//div[@class='modal-content']//span[text()='Тендер на закупку ТМЦ']")
    FIELD_TITLE_LOCATOR = ("xpath", "//um-input-field[contains(@class, 'field field--full-width' )]//input")
    FIELD_REGION_LOCATOR = ("xpath", "//input[@id='mat-chip-list-input-0']")
    CHOOSE_REGION_LOCATOR = ("xpath", "//div[@role='listbox']//span[contains(text(), 'Москва')]")

    FIELD_PURCHASE_CATEGORY_LOCATOR = ("xpath", "//input[@id='mat-chip-list-input-1']")
    CHOOSE_CATEGORY_LOCATOR = ("xpath", "//div/mat-option/span[@class='mat-option-text']")

    BUTTON_ADD_LOCATOR = ("xpath", "//um-grid-field[contains(@class, 'field_purchaseItems')]//span[text()= 'Добавить']")
