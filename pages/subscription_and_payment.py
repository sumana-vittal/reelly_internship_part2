from selenium.webdriver.common.by import By

from pages.base_page import Page


class SubscriptionPaymentPage(Page):

    SUBSCRIPTION_TITLE = (By.XPATH, "//div[text()='Subscription & payments']")
    UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, "[wized='upgradePlanButton']")
    BACK_BTN = (By.CSS_SELECTOR, "a.button-verify.margin-top-8")

    def subscription_payment_page_open(self):
        self.verify_partial_url('subscription')

    def verify_subscription_title(self):
        self.presence_of_element_located(*self.SUBSCRIPTION_TITLE)

    def verify_ugrade_back_btn(self):
        self.presence_of_element_located(*self.UPGRADE_PLAN_BTN)
        self.presence_of_element_located(*self.BACK_BTN)




