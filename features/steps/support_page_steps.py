from behave import given, when, then

@when("Click on support option.")
def click_support(context):
    context.app.settings_page.click_support()

@when("Switch to the new tab.")
def switch_support_tab(context):
    context.parent_window = context.driver.current_window_handle
    context.app.support_page.switch_to_new_window()

@then("Verify the right page support opens.")
def verify_support_page_opens(context):
    context.app.support_page.verify_support_page_opens()

@when("Go back.")
def go_back(context):
    context.driver.close()
    context.app.page.switch_to_window(context.parent_window)