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

    DEVELOPERS_TAB = (By.CSS_SELECTOR, "div[wized='marketTagDevelopers']")
    MARKET_PAGE_CARD = (By.CSS_SELECTOR, "a[wized='marketPageCard']")
    LICENSE_TAG = (By.CSS_SELECTOR, "//div[text()='License']")
    DEVELOPER_PAGE_MARKET_IMAGE = (By.CSS_SELECTOR, "img[wized='marketPageBackgraundPhoto']")

    ADD_COMPANY_BTN = (By.CSS_SELECTOR, "a.add-company-button")

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

#----------------------------------------------------------------------------------------------------------------------
    def click_on_developers(self):
        # wait for maket page to load
        self.presence_of_element_located(*self.MARKET_PROJECT_GRID)
        #click on Developers filter
        self.wait_element_clickable_click(*self.DEVELOPERS_TAB)

    def verify_license_tag(self):
        self.wait_for_all_visibility_elements_located(*self.DEVELOPER_PAGE_MARKET_IMAGE)
        # find all market grid card
        market_cards = self.find_elements(*self.MARKET_PAGE_CARD)
        print(len(market_cards))
        # check each card has license tag
        for card in market_cards:
            assert 'License' in card.text , f"This market card doesn't have License Tag."
# ----------------------------------------------------------------------------------------------------------------------

    def click_add_company_btn(self):
        self.wait_element_clickable_click(*self.ADD_COMPANY_BTN)

