from behave import given, when, then

@given("Open the main page https://soft.reelly.io/sign-up")
def open_main_page(context):
    context.app.main_page.open_main_page("https://soft.reelly.io/sign-up")

@when("Enter some test information in the registration input fields.")
def enter_registration_information(context):
    context.app.registration_page.enter_registration_data()

@then("Verify the right information is present.")
def verify_registration_informaiton(context):
    context.app.registration_page.verify_right_information()