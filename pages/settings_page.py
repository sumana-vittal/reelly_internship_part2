from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):

    ADD_A_PROJECT = (By.CSS_SELECTOR, "[href*='add-a-project'].page-setting-block")
    EDIT_PROFILE = (By.CSS_SELECTOR, "[href*='profile-edit']")
    COMMUNITY = (By.CSS_SELECTOR, "[href*='community'].page-setting-block")
    CONTACT_US = (By.CSS_SELECTOR, "[href*='contact-us'].page-setting-block")
    USER_GUIDE = (By.CSS_SELECTOR, "a[href*='user-guide'].page-setting-block")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "a[href*='password']")
    SUBSCRIPTION_AND_PAYMENT = (By.CSS_SELECTOR, "a[href *= 'subscription'].page-setting-block" )
    SUPPORT = (By.CSS_SELECTOR, "[href*='https://api.whatsapp.com']")
    NEWS = (By.CSS_SELECTOR, "[href*='https://t.me/reellydxb'].page-setting-block")
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, "a.page-setting-block")
    CONNECT_COMPANY_BUTTON = (By.XPATH, "//div[@class='settings-profile-block']//div[text()='Connect the company']")
    VERIFICATION = (By.CSS_SELECTOR, "a[href*='verification']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_a_project(self):
        self.click(*self.ADD_A_PROJECT)

    def click_edit_profile(self):
        self.click(*self.EDIT_PROFILE)

    def click_community(self):
        self.click(*self.COMMUNITY)

    def click_contact_us(self):
        self.click(*self.CONTACT_US)

    def click_user_guide(self):
        self.click(*self.USER_GUIDE)

    def click_change_password(self):
        self.click(*self.CHANGE_PASSWORD)

    def click_subscription_and_payment(self):
        self.click(*self.SUBSCRIPTION_AND_PAYMENT)

    def click_support(self):
        self.click(*self.SUPPORT)

    def click_news(self):
        self.click(*self.NEWS)

    def click_verification(self):
        self.click(*self.VERIFICATION)

    def verify_setting_page_opens(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def verify_settings_options(self, no_of_options):
        setting_options = self.find_elements(*self.SETTINGS_OPTIONS)
        assert str(len(setting_options)) == no_of_options, f"Should have {no_of_options} options under settings"

    def verify_connect_company_button(self):
        self.presence_of_element_located(*self.CONNECT_COMPANY_BUTTON)







