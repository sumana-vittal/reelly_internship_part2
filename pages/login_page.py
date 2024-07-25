from selenium.webdriver.common.by import By
from pages.base_page import Page


class Login(Page):

    # locators
    SIGN_IN = (By.CSS_SELECTOR, "[class='sing-in-text']")
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")

    def __init__(self, driver):
        super().__init__(driver)

    # open the main page with given URL
    def open_home_page(self):
        self.open("https://soft.reelly.io/sign-up")

    # Click on the sign in link
    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    # Enter the log in credentials and click on the continue button
    def login_details_and_click(self):
        self.input_text("vn.sumana@gmail.com", *self.EMAIL_FIELD)
        self.input_text("sReelly", *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)