from behave import given, when, then


@given('Open the main page')
def open_home_page(context):
    context.app.login.open_home_page()


@when("Click on the sign in")
def click_sign_in(context):
    context.app.login.click_sign_in()


@when("Log in to the page.")
def login_page(context):
    context.app.login.login_details_and_click()