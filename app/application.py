from pages.add_a_project_page import AddAProjectPage
from pages.base_page import Page
from pages.edit_profile_page import EditProfilePage
from pages.login_page import Login
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.settings_page import SettingsPage
from pages.side_panel_menu import SidePanelMenu

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
