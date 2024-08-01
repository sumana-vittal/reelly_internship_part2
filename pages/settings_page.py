from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):

    ADD_A_PROJECT = (By.CSS_SELECTOR, "[href*='add-a-project'].page-setting-block")
    EDIT_PROFILE = (By.CSS_SELECTOR, "[href*='profile-edit']")
    COMMUNITY = (By.CSS_SELECTOR, "[href*='community'].page-setting-block")

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_a_project(self):
        self.click(*self.ADD_A_PROJECT)

    def click_edit_profile(self):
        self.click(*self.EDIT_PROFILE)

    def click_community(self):
        self.click(*self.COMMUNITY)





