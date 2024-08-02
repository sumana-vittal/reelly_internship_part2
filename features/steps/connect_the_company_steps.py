from behave import given, when , then

@when("Click on 'Connect the company'")
def click_connect_the_company(context):
    context.app.side_panel_menu.click_connect_the_company()

@when("Switch the new tab.")
def switch_new_tab(context):
    context.app.connect_the_company.switch_tab()

@then("Verify the right tab opens.")
def verify_right_page_opened(context):
    context.app.connect_the_company.verify_connect_the_company_opened('book-presentation')
