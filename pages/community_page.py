from selenium.webdriver.common.by import By

from pages.base_page import Page


class CommunityPage(Page):

    CONTACT_SUPPORT_BTN = (By.XPATH, "//*[@class='d-version'] //*[text()='Contact support']")


    def __init__(self, driver):
        super().__init__(driver)

    def verify_right_url(self, expected_url_text):
        self.verify_partial_url(expected_url_text)

    def verify_contact_support(self):
        # self.presence_of_element_located(*self.CONTACT_SUPPORT_BTN)
        self.wait_element_clickable(*self.CONTACT_SUPPORT_BTN)

