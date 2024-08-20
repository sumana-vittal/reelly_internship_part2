from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactUs(Page):

    SOCIAL_ICONS = (By.CSS_SELECTOR, "a[href*='reelly'].contact-button")
    CONNECT_THE_COMPANY_BTN = (By.XPATH, "//div[@class='community-grid contact'] //div[text()='Connect the company']")

    social_icons_names = ['Instagram', 'Telegram', 'Youtube', 'Facebook', 'Twitter', 'TikTok', 'Pinterest', 'Snapchat',
                          'LinkedIn']

    def verify_social_icon(self):
        icons = self.find_elements(*self.SOCIAL_ICONS)
        if icons.count != 4:
            assert icons.count, f"Needs {icons.count} social icons to be present."
        else:
            for icon in icons:
                if icon.text not in self.social_icons_names:
                    assert icon.text, f"{icon.text} is not a social icon."

    def verify_connect_company_btn(self):
        self.wait_element_clickable(*self.CONNECT_THE_COMPANY_BTN)

    def verify_contact_page_opened(self, expected_url_text):
        self.verify_partial_url(expected_url_text)