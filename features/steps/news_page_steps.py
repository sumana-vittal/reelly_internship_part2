from behave import given, when, then

@when("Click on news option.")
def click_news(context):
    context.app.settings_page.click_news()

@then("Verify the right page news opens.")
def verify_news_page_opens(context):
    context.app.news_page.verify_news_page_opened()