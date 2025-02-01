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

# ----------------------------------------------------------------------------------------------------------------------

@when("Click on Developers filter at the top of the page.")
def click_on_developers(context):
    context.app.market_page.click_on_developers()

@then("Verify all cards has the license tag.")
def verify_license_tag(context):
    context.app.market_page.verify_license_tag()

# ----------------------------------------------------------------------------------------------------------------------

@when("Click on 'Add Company' button.")
def click_add_company_btn(context):
    context.app.market_page.click_add_company_btn()

@then("Verify the 'Add Company' page opens.")
def verify_add_company_page_opens(context):
    context.app.add_company_page.verify_add_company_page_opens()

@then("Verify the button 'Publish my company' is available.")
def verify_publish_my_company_btn(context):
    context.app.add_company_page.verify_publish_company_btn()