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

#----------------------------------------------------------------------------------------------------------------------
@then("Verify each product on this page contains a title and picture visible.")
def verify_product_title_picture(context):
    context.app.off_plan_page.verify_product_title_picture()

#----------------------------------------------------------------------------------------------------------------------

@when("Filter by sale status of 'Out of Stocks'.")
def filter_sale_status_out_of_stock(context):
    context.app.off_plan_page.filter_sale_status_out_of_stock()

@then("Verify each product contains the Out of Stocks tag.")
def verify_product_stock_tag(context):
    context.app.off_plan_page.verify_product_stock_tag(context.val)

#----------------------------------------------------------------------------------------------------------------------

@when("Click on the first product.")
def click_on_first_product(context):
    context.app.off_plan_page.click_on_first_product()

@then("Verify the one of three options of visualization 'architecture', 'interior', 'lobby' is present and are clickable")
def verify_product_visualization_present_and_clickable(context):
    context.app.project_page.verify_product_visualization_present_and_clickable()


#----------------------------------------------------------------------------------------------------------------------