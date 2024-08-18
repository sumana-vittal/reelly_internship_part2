from behave import given, when, then

@when("Click on Contact us option.")
def click_contact_us(context):
    context.app.settings_page.click_contact_us()

@then("Verify there are at least 4 social media icons.")
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_icon()

@then("Verify 'Connect the company' button is available and clickable")
def verify_connect_button(context):
    context.app.contact_us_page.verify_connect_company_btn()

@then("Verify the contact page opens.")
def verify_contact_page_opened(context):
    context.app.contact_us_page.verify_partial_url('contact-us')