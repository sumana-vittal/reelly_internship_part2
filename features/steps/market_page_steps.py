from behave import given, when, then

@when("Click on 'Market' at the left side menu.")
def click_on_market(context):
    context.app.market_page.click_on_market()

@then("Verify the Market page opens.")
def verify_market_page(context):
    context.app.market_page.verify_market_page()

@when("Go to the final page using pagination.")
def goto_final_market_page(context):
    context.app.market_page.goto_final_market_page()

@when("Go to the first page using pagination.")
def goto_first_market_page(context):
    context.app.market_page.goto_first_market_page()