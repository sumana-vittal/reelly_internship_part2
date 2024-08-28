from behave import given, when, then

@when("Click on Change password option.")
def click_change_password(context):
    context.app.settings_page.click_change_password()

@then("Verify the change password page opens.")
def change_password_page_opened(context):
    context.app.change_password.verify_change_password_page_opened('password')

@then("Add some test password to the input fields.")
def test_password_field_data(context):
    context.app.change_password.input_password_test_data()

@then("Verify the 'Change password' button is available.")
def verify_change_password_btn_present(context):
    context.app.change_password.verify_change_password_btn_present()