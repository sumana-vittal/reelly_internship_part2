Feature: Test Scenarios for the registration page.

  Scenario: Verify test data for the registration page
    Given Open the main page https://soft.reelly.io/sign-up
    When Enter some test information in the registration input fields.
    Then Verify the right information is present.