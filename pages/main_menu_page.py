from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainMenuPage(Page):

    SELECTED_LANGUAGE = (By.CSS_SELECTOR, "[id='w-dropdown-toggle-0']")
    RU_LANG = (By.CSS_SELECTOR, "[id='w-dropdown-list-0']")

    def __init__(self, driver):
        super().__init__(driver)

    def change_language(self):
        action = ActionChains(self.driver)
        element = self.find_element(*self.SELECTED_LANGUAGE)
        # move to the element and click then perform the operation
        action.move_to_element(element)
        element = self.find_element(*self.RU_LANG)
        action.move_to_element(element)
        action.click()
        action.perform()

    def verify_language_change(self):
        self.verify_text('RU',*self.SELECTED_LANGUAGE)