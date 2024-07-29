from selenium.webdriver.common.by import By

from pages.base_page import Page


class SidePanelMenu(Page):

    SETTINGS_SIDE_MENU_LINK = (By.CSS_SELECTOR, "[href*='settings'][class*='menu-button-block']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_settings(self):
        self.click(*self.SETTINGS_SIDE_MENU_LINK)


