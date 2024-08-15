from behave import given, when, then

@when("Change the language of the page to Russian. The option will be 'RU' which is the list of the languages.")
def change_language(context):
    context.app.side_panel_menu.click_main_menu()
    context.app.main_menu_page.change_language()

@then("Verify the language has changed.")
def verify_language_changes(context):
    context.app.main_menu_page.verify_language_change()
