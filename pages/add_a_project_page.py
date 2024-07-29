from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class AddAProjectPage(Page):

    NAME_FIELD = (By.ID, "Your-name")
    COMPANY_NAME = (By.ID, "Your-company-name")
    COMPANY_ROLE =(By.ID, "Role")
    COMPANY_AGE=(By.ID, "Age-of-the-company")
    PROJECT_LOCATION = (By.ID, "Country")
    PROJECT_NAME = (By.ID, "Name-project")
    PHONE =(By.ID, "Phone")
    EMAIL=(By.ID, "Email-add-project")
    SEND_APPLICATION_BTN = (By.CSS_SELECTOR, "[value='Send an application']")

    def __int__(self, driver):
        super().__int__(driver)

    def verify_right_url(self):
        self.verify_partial_url("add-a-project")

    def input_project_data(self):
        self.input_text("James", *self.NAME_FIELD)
        self.input_text("JDevelopers", *self.COMPANY_NAME)
        self.input_text("Developers", *self.COMPANY_ROLE)
        self.input_text("5", *self.COMPANY_AGE)
        self.input_text("Dubai", *self.PROJECT_LOCATION)
        self.input_text("Serene", *self.PROJECT_NAME)
        self.input_text("000-000-0000", *self.PHONE)
        self.input_text("aaabbbccc@abc.com", *self.EMAIL)


    def verify_right_data(self):
        #sleep(10)
        self.verify_attribute_value("James", *self.NAME_FIELD)
        self.verify_attribute_value("JDevelopers", *self.COMPANY_NAME)
        self.verify_attribute_value("Developers", *self.COMPANY_ROLE)
        self.verify_attribute_value("5", *self.COMPANY_AGE)
        self.verify_attribute_value("Dubai", *self.PROJECT_LOCATION)
        self.verify_attribute_value("Serene", *self.PROJECT_NAME)
        self.verify_attribute_value("000-000-0000", *self.PHONE)
        self.verify_attribute_value("aaabbbccc@abc.com", *self.EMAIL)

    def verify_send_application(self):
        self.presence_of_element_located(*self.SEND_APPLICATION_BTN)
        self.wait_element_clickable(*self.SEND_APPLICATION_BTN)


