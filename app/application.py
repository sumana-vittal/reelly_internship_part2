from pages.base_page import Page
from pages.login_page import Login


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.login = Login(driver)
