from selenium.webdriver.common.by import By

from pages.base_page import Page


class EditProfilePage(Page):
    YOUR_NAME = (By.ID, "Fullname")
    PHONE_NUMBER = (By.ID, "number")
    COMPANY = (By.ID, "Company-name")
    JOINING_DATE = (By.ID, "When-joined-company-2")
    YOUR_ROLE = (By.ID, "field")
    YOUR_POSITION = (By.ID, "Position")
    CONTACT_EMAIL = (By.ID, "Email-2")
    LANGUAGES = (By.ID, "Languages")
    LICENSE_NUMBER = (By.ID, "When-joined-company")
    SOCIAL_MEDIA = (By.ID, "Email")
    CLOSE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".profile-button-block [class*='close-button']")
    SAVE_CHANGES_PROFILE_BUTTON = (By.CSS_SELECTOR, ".profile-button-block .save-changes-button")

    # social_icons_names = ['Instagram', 'Telegram', 'Youtube', 'Facebook', 'Twitter', 'TikTok', 'Pinterest', 'Snapchat',
    #                       'LinkedIn']

    def __int__(self, driver):
        super().__int__(driver)

    def enter_profile_data(self):
        self.clear_text(*self.YOUR_NAME)
        self.input_text("test+sumana+careerist", *self.YOUR_NAME)
        self.clear_text(*self.PHONE_NUMBER)
        self.input_text("246+test+careerist", *self.PHONE_NUMBER)
        self.clear_text(*self.COMPANY)
        self.input_text("test", *self.COMPANY)
        self.input_text("2023 Q3", *self.JOINING_DATE)
        self.input_text("Developer", *self.YOUR_ROLE)
        self.input_text("Seller", *self.YOUR_POSITION)
        self.clear_text(*self.CONTACT_EMAIL)
        self.input_text("test@test.com", *self.CONTACT_EMAIL)
        self.clear_text(*self.LANGUAGES)
        self.input_text("English", *self.LANGUAGES)
        self.clear_text(*self.LICENSE_NUMBER)
        self.input_text("00000", *self.LICENSE_NUMBER)
        self.clear_text(*self.SOCIAL_MEDIA)
        self.input_text("https://www.careerist.com", *self.SOCIAL_MEDIA)

    def verify_right_profile_information(self):
        self.verify_attribute_value(" test+sumana+careerist", *self.YOUR_NAME)
        self.verify_attribute_value("246+test+careerist", *self.PHONE_NUMBER)
        self.verify_attribute_value("test", *self.COMPANY)
        self.verify_attribute_value("2023 Q3", *self.JOINING_DATE)
        self.verify_attribute_value("Developer", *self.YOUR_ROLE)
        self.verify_attribute_value("Seller", *self.YOUR_POSITION)
        self.verify_attribute_value("test@test.com", *self.CONTACT_EMAIL)
        self.verify_attribute_value("English", *self.LANGUAGES)
        self.verify_attribute_value("00000", *self.LICENSE_NUMBER)
        self.verify_attribute_value("https://www.careerist.com", *self.SOCIAL_MEDIA)


    def verify_profile_buttons(self):
        self.presence_of_element_located(*self.CLOSE_PROFILE_BUTTON)
        self.wait_element_clickable(*self.CLOSE_PROFILE_BUTTON)
        self.presence_of_element_located(*self.SAVE_CHANGES_PROFILE_BUTTON)
        self.wait_element_clickable_click(*self.SAVE_CHANGES_PROFILE_BUTTON)

