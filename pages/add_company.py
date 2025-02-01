from selenium.webdriver.common.by import By

from pages.base_page import Page


class AddCompanyPage(Page):

    PUBLISH_COMPANY = (By.CSS_SELECTOR, "div.buttons-block-market a.publish-button")

    def verify_add_company_page_opens(self):
        self.verify_partial_url("presentation-for-the-agency")

    def verify_publish_company_btn(self):
        self.presence_of_element_located(*self.PUBLISH_COMPANY)

