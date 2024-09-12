from pages.base_page import Page


class NewsPage(Page):

    def verify_news_page_opened(self):
        self.verify_partial_url("t.me")