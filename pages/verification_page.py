from selenium.webdriver.common.by import By

from pages.base_page import Page


class VerificationPage(Page):

    UPLOAD_IMAGE_BTN = (By.CSS_SELECTOR, "div.upload-button-2")
    NEXT_STEP_BTN = (By.CSS_SELECTOR, "a[wized='nextButtonStep0']")

    def verify_verification_page(self):
        self.verify_partial_url("verification")

    def verify_verification_buttons(self):
        self.wait_for_visibility_of_element_located(*self.UPLOAD_IMAGE_BTN)
        self.wait_for_visibility_of_element_located(*self.NEXT_STEP_BTN)
