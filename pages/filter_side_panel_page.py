from selenium.webdriver.common.by import By

from pages.base_page import Page


class FilterPage(Page):

    WANT_TO_SELL = (By.CSS_SELECTOR, "[wized='ListingTypeSell']")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")

    def filter_by_want_to_sell(self):
        self.click(*self.WANT_TO_SELL)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER)
