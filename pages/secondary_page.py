import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class SecondaryPage(Page):

    PAGINATION = (By.CSS_SELECTOR, ".pagination-text")
    TOTAL_PAGE_COUNT = (By.CSS_SELECTOR, "[wized='totalPageProperties']")
    CURRENT_PAGE_COUNT = (By.XPATH, "//div[@wized='currentPageProperties']")
    NEXT_PAGE = (By.CSS_SELECTOR,"[wized='nextPageMLS']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "[wized='previousPageMLS']")

    FILTER_BUTTON = (By.CSS_SELECTOR, ".filter-text")
    WANT_TO_SELL_TAG = (By.XPATH, "//div[contains(@class, 'tag-text-filters') and text()='Want to sell']")
    WANT_TO_SELL = (By.CSS_SELECTOR, "div[wized='ListingTypeSell']")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    LISTING_SALE_TAGS = (By.CSS_SELECTOR, "div[wized='listingCardMLS']")
    SALE_TAG = (By.CSS_SELECTOR, "div.for-sale-tag")


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

    def click_filter(self):
        self.wait_element_clickable_click(*self.FILTER_BUTTON)

    def filter_by_want_to_sell(self):
        # print(self.presence_of_element_located(*self.WANT_TO_SELL))
        self.wait_element_clickable_click(*self.FILTER_BUTTON)# previous click is not recognizing though executing, hence clicking again
        self.wait_element_clickable_click(*self.WANT_TO_SELL_TAG)
        # time.sleep(3)

    def click_apply_filter(self):
        self.wait_element_clickable_click(*self.APPLY_FILTER)
        # time.sleep(1)


    def verify_sale_tag(self):
        # listing_elements = self.find_elements(*self.LISTING_SALE_TAGS)
        listing_elements = self.wait_for_all_visibility_elements_located(*self.LISTING_SALE_TAGS)
        print(len(listing_elements))
        for list_card in listing_elements:
            sale_tag = list_card.find_element(*self.SALE_TAG).text
            assert 'For sale' in sale_tag, f"Expected 'For sale' tag but didn't find."
            # print(sale_tag)








