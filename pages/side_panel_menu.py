from selenium.webdriver.common.by import By

from pages.base_page import Page


class SidePanelMenu(Page):

    SETTINGS_SIDE_MENU_LINK = (By.CSS_SELECTOR, "[href*='settings'][class*='menu-button-block']")
    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class*='get-free-period']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_settings(self):
        self.click(*self.SETTINGS_SIDE_MENU_LINK)

    def click_connect_the_company(self):
        self.click(*self.CONNECT_THE_COMPANY_BTN )


