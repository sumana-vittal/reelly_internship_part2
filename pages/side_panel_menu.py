from selenium.webdriver.common.by import By

from pages.base_page import Page


class SidePanelMenu(Page):

    SETTINGS_SIDE_MENU_LINK = (By.CSS_SELECTOR, "[href*='settings'][class*='menu-button-block']")
    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class*='get-free-period']")
    MAIN_MENU_LINK = (By.XPATH, "//div[text()='Main menu']")
    SECONDARY_MENU_LINK = (By.CSS_SELECTOR, "a[href='/secondary-listings'].menu-button-block")

    def __init__(self,driver):
        super().__init__(driver)

    def click_settings(self):
        self.presence_of_element_located(*self.SETTINGS_SIDE_MENU_LINK)
        self.click(*self.SETTINGS_SIDE_MENU_LINK)

    def click_connect_the_company(self):
        self.click(*self.CONNECT_THE_COMPANY_BTN )

    def click_main_menu(self):
        self.click(*self.MAIN_MENU_LINK)

    def click_secondary_menu(self):
        self.click(*self.SECONDARY_MENU_LINK)



