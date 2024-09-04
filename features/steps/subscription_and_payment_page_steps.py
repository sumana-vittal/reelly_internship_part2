from behave import given, when, then

@when("Click on Subscription & payments option.")
def click_payment_and_subscription(context):
    context.app.settings_page.click_subscription_and_payment()

@then("Verify the 'subscription and payment' page opens.")
def verify_subscription_and_payment_page_opens(context):
    context.app.subscription_payment.subscription_payment_page_open()

@then("Verify title 'Subscription & payments' is visible.")
def verify_title_subscription_visible(context):
    context.app.subscription_payment.verify_subscription_title()

@then("Verify 'back' and 'upgrade plan' buttons are available.")
def verify_back_and_upgrade_btns(context):
    context.app.subscription_payment.verify_ugrade_back_btn()