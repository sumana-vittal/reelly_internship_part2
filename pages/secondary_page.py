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
    WANT_TO_BUY_TAG = (By.XPATH, "//div[contains(@class, 'tag-text-filters') and text()='Want to buy']")
    APPLY_FILTER = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    LISTING_SALE_BUY_TAGS = (By.CSS_SELECTOR, "div[wized='listingCardMLS']")
    SALE_BUY_TAG = (By.CSS_SELECTOR, "div.for-sale-tag")

    PRICE_FROM_AMOUNT = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    PRICE_TO_AMOUNT = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    PRICE_LISTED = (By.CSS_SELECTOR, "div.number-price-text")


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
        listing_elements = self.wait_for_all_visibility_elements_located(*self.LISTING_SALE_BUY_TAGS)
        print(len(listing_elements))
        for list_card in listing_elements:
            sale_tag = list_card.find_element(*self.SALE_BUY_TAG).text
            assert 'For sale' in sale_tag, f"Expected 'For sale' tag but didn't find."
            # print(sale_tag)

# ----------------------------------------------------------------------------------------------------------------------

    def filter_by_want_to_buy(self):
       self.wait_element_clickable_click(*self.FILTER_BUTTON)# previous click is not recognizing though executing, hence clicking again
       self.wait_element_clickable_click(*self.WANT_TO_BUY_TAG)

    def verify_want_to_buy_tag(self):
        listing_elements = self.wait_for_all_visibility_elements_located(*self.LISTING_SALE_BUY_TAGS)
        print(len(listing_elements))
        for list_card in listing_elements:
            tags = list_card.find_element(*self.SALE_BUY_TAG).text
            assert 'Want to buy' in tags, f"Expected 'Want to buy' tag but didn't find."

# ----------------------------------------------------------------------------------------------------------------------

    def filter_by_price_range(self):
        self.wait_element_clickable_click(*self.FILTER_BUTTON)
        self.input_text("1200000", *self.PRICE_FROM_AMOUNT)
        self.input_text("2000000", *self.PRICE_TO_AMOUNT)
        self.wait_element_clickable_click(*self.APPLY_FILTER)

    def verify_filtered_price_range(self):
        price_list = self.find_elements(*self.PRICE_LISTED)
        for price in price_list:
            amount = price.text.replace('AED', '').replace(',','')
            assert int(amount) in range(1200000, 2000001), f"Price not in range!"










