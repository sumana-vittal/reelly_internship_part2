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






