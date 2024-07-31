from selenium.webdriver.common.by import By

from pages.base_page import Page


class RegistrationPage(Page):

    FULL_NAME = (By.ID, "Full-Name")
    PHONE = (By.ID, "phone2")
    EMAIL = (By.ID, "Email-3")
    PASSWORD = (By.ID, "field")
    COMPANY_NAME = (By.ID, "Company-website")
    ROLE = (By.ID, "Role")
    POSITION = (By.ID, "Position")
    COUNTRY = (By.ID, "country-select")
    COMPANY_SIZE = (By.ID, "Agents-amount-2")
    PRIVACY_POLICY_CHECKBOX = (By.ID, "checkbox")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".login-button")


    def __int__(self, driver):
        super().__int__(driver)

    def enter_registration_data(self):
        self.input_text("James", *self.FULL_NAME)
        self.input_text("0000000000", *self.PHONE)
        self.clear_text(*self.EMAIL)
        self.input_text("test@test.com", *self.EMAIL)
        self.clear_text(*self.PASSWORD)
        self.input_text("abcd123", *self.PASSWORD)
        self.input_text("abc", *self.COMPANY_NAME)
        self.select_dropdown_value('Broker', *self.ROLE)
        self.select_dropdown_value('Seller / Manager', *self.POSITION )
        self.select_dropdown_value('United States of America', *self.COUNTRY)
        self.select_dropdown_value('50-100', *self.COMPANY_SIZE)
        self.checkbox_click(*self.PRIVACY_POLICY_CHECKBOX)

    def verify_right_information(self):
        self.verify_attribute_value("James", *self.FULL_NAME)
        self.verify_attribute_value("0000000000", *self.PHONE)
        self.verify_attribute_value("test@test.com", *self.EMAIL)
        self.verify_attribute_value("abcd123", *self.PASSWORD)
        self.verify_attribute_value("abc", *self.COMPANY_NAME)
        self.get_dropdown_value('Broker', *self.ROLE)
        self.get_dropdown_value('Seller / Manager', *self.POSITION)
        self.get_dropdown_value('United States of America', *self.COUNTRY)
        self.get_dropdown_value('50-100', *self.COMPANY_SIZE)
        self.is_checkbox_selected(*self.PRIVACY_POLICY_CHECKBOX)

