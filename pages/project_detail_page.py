from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProjectPage(Page):
    DEVELOPER_NAME = (By.CSS_SELECTOR, ".developer-name")
    VISUALIZATION_TAB = (By.CSS_SELECTOR, ".tab")

    def verify_product_visualization_present(self, visualization_tabs):
        self.presence_of_element_located(*self.DEVELOPER_NAME)  # page to load
        tabs = self.find_elements(*self.VISUALIZATION_TAB)
        web_element_tabs = [element.text for element in tabs]
        assert any(e in visualization_tabs for e in web_element_tabs), f"Visualization options are missing."

    def verify_visualization_option_clickable(self, visualization_tabs):
        tabs = self.find_elements(*self.VISUALIZATION_TAB)
        for tab in tabs:
            if tab.text != "":
                assert tab.is_displayed() and tab.is_enabled(), f"Visualization Option is not enabled."
