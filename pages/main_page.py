from pages.base_page import Page


class MainPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open("https://soft.reelly.io/")
