from pages.base_page import Page


class ConnectTheCompany(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def switch_tab(self):
        self.switch_to_new_window();
        #print(self.driver.current_url)

    def verify_connect_the_company_opened(self, expected_text):
        self.verify_partial_url(expected_text)