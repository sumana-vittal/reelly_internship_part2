from behave import given, when, then

@then("Verify the right page verification opens.")
def verify_verification_page(context):
    context.app.verification_page.verify_verification_page()

@then("Verify 'upload image' and 'Next step' buttons are available.")
def verify_verification_buttons(context):
    context.app.verification_page.verify_verification_buttons()
