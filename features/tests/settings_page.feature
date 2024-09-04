Feature: Test Scenarios for the setting page.

  Scenario: verify Add a project in Settings
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on settings option.
      And Click on Add a project.
      Then Verify the right page opens.
      When Add some test information to the input fields.
      Then Verify the right information is present in the input fields.
      Then Verify 'Send an application' button is available and clickable.

  Scenario: Verify Data Edit profile in Settings
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on settings option.
     And Click on Edit profile option.
     And Enter some test information in the input fields.
     Then Check the right information is present in the input fields.
     Then Check 'Close' and 'Save Changes' buttons are available and clickable.

  Scenario: Verify Community Page data
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on settings option.
     And Click on Community option.
     Then Verify the Community page opens.
     Then Verify 'Contact support' button is available and clickable.

  Scenario: Verify Contact us page data
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on settings option.
      And Click on Contact us option.
      Then Verify the contact page opens.
      And Verify there are at least 4 social media icons.
      And Verify 'Connect the company' button is available and clickable

  Scenario: Verify User Guide page data
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on settings option.
     And Click on User Guide option.
     Then Verify the user guide page opens.
     And Verify all lesson videos contain titles

  Scenario: Verify Change Password page
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on settings option.
    And Click on Change password option.
    Then Verify the change password page opens.
    And Add some test password to the input fields.
    And Verify the 'Change password' button is available.

  Scenario:  User can open Subscription & payments page
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on settings option.
    And Click on Subscription & payments option.
    Then Verify the 'subscription and payment' page opens.
    And Verify title 'Subscription & payments' is visible.
    And Verify 'back' and 'upgrade plan' buttons are available.
