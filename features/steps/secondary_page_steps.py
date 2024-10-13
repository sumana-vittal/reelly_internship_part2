from behave import given, when, then

@when("Click on Secondary option at the left side menu.")
def click_on_secondary_side_menu(context):
    context.app.side_panel_menu.click_secondary_menu()

@then("Verify the Secondary page opens.")
def verify_secondary_page_opens(context):
    context.app.secondary_page.verify_secondary_page_opens('secondary')

@then("Go to the final page using the pagination button.")
def goto_final_page(context):
    context.app.secondary_page.goto_final_page()

@then("Go back to the first page using the pagination button.")
def goto_first_page(context):
    context.app.secondary_page.goto_first_page()
