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