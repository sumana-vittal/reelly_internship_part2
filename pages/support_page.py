from pages.base_page import Page


class SupportPage(Page):

    def switch_tab(self):
        self.switch_to_new_window()

    def verify_support_page_opens(self):
        self.verify_partial_url("api.whatsapp.com")


