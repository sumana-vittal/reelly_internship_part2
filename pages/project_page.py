from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProjectPage(Page):
    DEVELOPER_NAME = (By.CSS_SELECTOR, ".developer-name")
    VISUALIZATION_TAB = (By.CSS_SELECTOR, ".tab")

    def verify_product_visualization_present_and_clickable(self):
        visualization = ["Architecture", "Interior", "Lobby"]  # all visualization
        web_element_tabs = []  # to store each product's visualization
        bclickable = False  # to check button status

        self.presence_of_element_located(*self.DEVELOPER_NAME)  # page to load
        tabs = self.find_elements(*self.VISUALIZATION_TAB)

        for tab in tabs:
            if tab.text != "":
                web_element_tabs.append(tab.text)
                bclickable = tab.is_displayed() and tab.is_enabled()

        assert any(e in visualization for e in web_element_tabs), f"Visualization options are missing."
        assert bclickable == True, f"Visualization options are not enabled."
