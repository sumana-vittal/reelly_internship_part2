import time

from selenium.webdriver.common.by import By

from pages.base_page import Page


class OffPlanPage(Page):

    OFF_PLAN_MENU = (By.CSS_SELECTOR, ".menu-twobutton")
    OFF_PLAN_PAGE = (By.CSS_SELECTOR, "div.game-menu-block .w--current")
    FIRST_PAGE_COUNT = (By.CSS_SELECTOR, "div[wized='currentPageProperties']")
    FINAL_PAGE_COUNT = (By.CSS_SELECTOR, "div[wized='totalPageProperties']")
    PREVIOUS_PAGE = (By.CSS_SELECTOR, "div[wized='previousPageProperties']")
    NEXT_PAGE = (By.CSS_SELECTOR, "a[wized='nextPageProperties']")

    FILTER_BTN = (By.CSS_SELECTOR, ".points-block-game .filter-text")
    FROM_FILTER_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_FILTER_PRICE = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    FILTERED_PRICE_RANGE = (By.CSS_SELECTOR, "div.price-value")
    PROJECT_BLOCK = (By.CSS_SELECTOR, ".cards-properties")

    PROJECTS = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    PROJECT_IMAGE = (By.CSS_SELECTOR, "div.project-image")
    PROJECT_TITLE = (By.CSS_SELECTOR, "div.project-name")

    def click_off_plan_menu(self):
        self.wait_element_clickable_click(*self.OFF_PLAN_MENU)

    def verify_off_plan_page(self):
        self.presence_of_element_located(*self.OFF_PLAN_PAGE)


    def goto_first_off_plan_page(self):
        first_page = self.find_element(*self.FIRST_PAGE_COUNT)

        time.sleep(2)  # required for the page to  load
        current_page = int(first_page.text)
        print(current_page)

        self.pagination(current_page, 1, -1, *self.PREVIOUS_PAGE)

    def goto_final_off_plan_page(self):
        first_page = self.find_element(*self.FIRST_PAGE_COUNT)
        final_page = self.find_element(*self.FINAL_PAGE_COUNT)

        time.sleep(2)  # required for the page to  load
        current_page = int(first_page.text)
        total_count = int(final_page.text)
        print(current_page, total_count)

        self.pagination(current_page, total_count, 1, *self.NEXT_PAGE)

    def filter_project_by_price_range(self):
        # self.wait_element_clickable_click(*self.FILTER_BTN)
        time.sleep(1) # needed because flaky internet
        self.presence_of_element_located(*self.PROJECT_BLOCK)
        self.wait_element_clickable_click(*self.FILTER_BTN)
        self.input_text("1200000", *self.FROM_FILTER_PRICE)
        self.input_text("2000000", *self.TO_FILTER_PRICE)
        # time.sleep(3)
        self.wait_element_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_price_in_range(self):
        time.sleep(5) # needed because flaky internet
        # self.presence_of_element_located(*self.PROJECT_BLOCK)
        price_lists  = self.find_elements(*self.FILTERED_PRICE_RANGE)
        print(len(price_lists))
        for price in price_lists:
            price_amount = int(price.text.replace('AED ','').replace(',', ''))
            # print(price_amount)
            assert 1200000 < price_amount < 2000000, f"Price should be in the range 1200000 to 2000000."

    def verify_product_title_picture(self):
        time.sleep(5) # for page to load
        # self.presence_of_element_located(*self.PROJECTS) # external page load not working
        projects = self.find_elements(*self.PROJECTS)
        # print(len(projects))
        for project in projects:
            image = project.find_element(*self.PROJECT_IMAGE)
            assert image.is_displayed(), f"Doesn't contain image."
            title = project.find_element(*self.PROJECT_TITLE)
            assert title.text != "", f"Doesn't contain title."





