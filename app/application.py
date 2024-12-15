from pages.add_a_project_page import AddAProjectPage
from pages.base_page import Page
from pages.change_password_page import ChangePassword
from pages.community_page import CommunityPage
from pages.connect_the_company_page import ConnectTheCompany
from pages.contact_us_page import ContactUs
from pages.edit_profile_page import EditProfilePage
from pages.login_page import Login
from pages.main_menu_page import MainMenuPage
from pages.main_page import MainPage
from pages.news_page import NewsPage
from pages.off_plan_page import OffPlanPage
from pages.project_detail_page import ProjectPage
from pages.registration_page import RegistrationPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.side_panel_menu import SidePanelMenu
from pages.subscription_and_payment import SubscriptionPaymentPage
from pages.support_page import SupportPage
from pages.user_guide_page import UserGuidePage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.login = Login(driver)
        self.main_page = MainPage(driver)
        self.side_panel_menu = SidePanelMenu(driver)
        self.settings_page = SettingsPage(driver)
        self.add_a_project = AddAProjectPage(driver)
        self.edit_profile = EditProfilePage(driver)
        self.registration_page = RegistrationPage(driver)
        self.community_page = CommunityPage(driver)
        self.connect_the_company = ConnectTheCompany(driver)
        self.main_menu_page = MainMenuPage(driver)
        self.contact_us_page = ContactUs(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.change_password = ChangePassword(driver)
        self.subscription_payment = SubscriptionPaymentPage(driver)
        self.support_page = SupportPage(driver)
        self.news_page = NewsPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.project_detail_page = ProjectPage(driver)
