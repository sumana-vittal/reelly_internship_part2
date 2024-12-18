import time

from selenium.webdriver.common.by import By

from pages.base_page import Page


class MarketPage(Page):

    MARKET_SIDE_MENU_LINK = (By.CSS_SELECTOR, "a[href='/market-companies'].menu-button-block")
    MARKET_PROJECT_GRID = (By.CSS_SELECTOR, "div.market-copmany-grid")
    NEXT_PAGE = (By.CSS_SELECTOR, "a[wized='nextPageMarket']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "div[wized='previousPageMarket']")
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, "div[wized='currentPageMarket']")
    FINAL_PAGE_COUNT = (By.CSS_SELECTOR, "div[wized='totalPageMarket']")

    def click_on_market(self):
        self.wait_element_clickable_click(*self.MARKET_SIDE_MENU_LINK)

    def verify_market_page(self):
        # wait for page to load
        self.presence_of_element_located(*self.MARKET_PROJECT_GRID)
        # verify the link
        self.verify_partial_url('market-companies')

    def goto_final_market_page(self):
        initial_value = self.find_element(*self.CURRENT_PAGE_COUNT)
        final_value = self.find_element(*self.FINAL_PAGE_COUNT)
        time.sleep(2)  # required for the page to  load
        initial_count = int(initial_value.text)
        final_count = int(final_value.text)
        print(initial_count,final_count)
        self.pagination(initial_count, final_count , 1, *self.NEXT_PAGE)

    def goto_first_market_page(self):
        initial_value = int(self.find_element(*self.CURRENT_PAGE_COUNT).text)
        time.sleep(2)  # required for the page to  load
        print(initial_value)
        self.pagination(initial_value, 1, -1, *self.PREVIOUS_PAGE)
