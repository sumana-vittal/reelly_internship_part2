from behave import given, when, then

@given("Open the main page https://soft.reelly.io")
def open_main_page(context):
    context.app.main_page.open_main_page("https://soft.reelly.io")

@when("Click on settings option.")
def click_settings(context):
    context.app.side_panel_menu.click_settings()

@when("Click on Add a project.")
def click_add_a_project(context):
    context.app.settings_page.click_add_a_project()

@then("Verify the right page opens.")
def verify_right_url(context):
    context.app.add_a_project.verify_right_url()

@when("Add some test information to the input fields.")
def input_test_data(context):
    context.app.add_a_project.input_project_data()

@then("Verify the right information is present in the input fields.")
def verify_right_information(context):
    context.app.add_a_project.verify_right_data()

@then("Verify 'Send an application' button is available and clickable.")
def verify_send_application_btn(context):
    context.app.add_a_project.verify_send_application()

#----------------------------------------------------------------------------------------------------------------

# steps for the edit profile
@when("Click on Edit profile option.")
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile()

@when("Enter some test information in the input fields.")
def enter_test_data(context):
    context.app.edit_profile.enter_profile_data()

@then("Check the right information is present in the input fields.")
def verify_profile_information(context):
    context.app.edit_profile.verify_right_profile_information()

@then("Check 'Close' and 'Save Changes' buttons are available and clickable.")
def verify_profile_btns(context):
    context.app.edit_profile.verify_profile_buttons()




