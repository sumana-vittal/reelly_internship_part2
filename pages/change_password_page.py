from selenium.webdriver.common.by import By

from pages.base_page import Page


class ChangePassword(Page):

    ENTER_PASSWORD = (By.CSS_SELECTOR, "#Enter-new-password")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#Repeat-password")
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "[wized='changePasswordButton']")

    def verify_change_password_page_opened(self, expected_url_text):
        self.verify_partial_url(expected_url_text)

    def input_password_test_data(self):
        self.input_text("passTest", *self.ENTER_PASSWORD)
        self.input_text("passTest", *self.REPEAT_PASSWORD)

    def verify_change_password_btn_present(self):
        self.presence_of_element_located(*self.CHANGE_PASSWORD_BTN)


