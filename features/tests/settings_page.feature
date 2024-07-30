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