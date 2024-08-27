from behave import given, when, then

@when("Click on User Guide option.")
def click_user_guide(context):
    context.app.settings_page.click_user_guide()

@then("Verify the user guide page opens.")
def verify_user_guide_opens(context):
    context.app.user_guide_page.verify_user_guide_opens()

@then("Verify all lesson videos contain titles")
def verify_video_titles(context):
    context.app.user_guide_page.verify_video_titles()