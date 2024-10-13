import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import Page


class SecondaryPage(Page):

    PAGINATION = (By.CSS_SELECTOR, ".pagination-text")
    TOTAL_PAGE_COUNT = (By.CSS_SELECTOR, "[wized='totalPageProperties']")
    CURRENT_PAGE_COUNT = (By.XPATH, "//div[@wized='currentPageProperties']")
    NEXT_PAGE = (By.CSS_SELECTOR,"[wized='nextPageMLS']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "[wized='previousPageMLS']")
    def verify_secondary_page_opens(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def goto_final_page(self):
        l = self.find_element(*self.CURRENT_PAGE_COUNT)
        total_page_count = self.find_element(*self.TOTAL_PAGE_COUNT)

        time.sleep(2) # required for the page to  load
        current_page = int(l.text)
        total_count = int(total_page_count.text)
        print(current_page, total_count)

        self.pagination(current_page, total_count, 1, *self.NEXT_PAGE)

        # time.sleep(2)
        print(l.text)

    def goto_first_page(self):
        l = self.find_element(*self.CURRENT_PAGE_COUNT)

        time.sleep(2) # required for the page to  load
        current_page = int(l.text)
        print(current_page)

        self.pagination(current_page, 1, -1, *self.PREVIOUS_PAGE)

        time.sleep(2)
        print(l.text)

