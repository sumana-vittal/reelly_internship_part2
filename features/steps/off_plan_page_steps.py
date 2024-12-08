from behave import given, when, then

@when("Click on off plan option at the left side menu.")
def click_off_plan_menu(context):
    context.app.off_plan_page.click_off_plan_menu()

@then("Verify the off-plan page opens.")
def verify_off_plan_page_opens(context):
    context.app.off_plan_page.verify_off_plan_page()

@when("Go to the final page using the pagination button.")
def go_to_off_plan_final_page(context):
    context.app.off_plan_page.goto_final_off_plan_page()

@when("Go back to the first page using the pagination button.")
def go_to_off_plan_first_page(context):
    context.app.off_plan_page.goto_first_off_plan_page()

#-----------------------------------------------------------------------------------------------------------------

@when("Filter the projects by price range from 1200000 to 2000000 AED.")
def filter_project_by_price_range(context):
    context.app.off_plan_page.filter_project_by_price_range()

@then("Verify the price in all cards is in the range (1200000 - 2000000).")
def verify_price_in_range(context):
    context.app.off_plan_page.verify_price_in_range()