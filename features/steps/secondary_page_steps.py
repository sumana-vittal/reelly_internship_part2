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

#-----------------------------------------------------------------------------------------------------------------
@when("Click on Filters.")
def click_filter(context):
    context.app.secondary_page.click_filter()

@when("Filter the products by 'want to sell'.")
def filter_by_want_to_sell(context):

    context.app.secondary_page.filter_by_want_to_sell()

@when("Click on Apply Filter.")
def apply_filter(context):
    context.app.secondary_page.click_apply_filter()

@then("Verify all cards have 'for sale' tag.")
def verify_sale_tag(context):
    context.app.secondary_page.verify_sale_tag()