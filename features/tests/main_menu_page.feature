Feature: Test Scenario for the Main menu

  Scenario: Verify the language selection and changes.
   Given Open the main page https://soft.reelly.io
   When Log in to the page.
   When Change the language of the page to Russian. The option will be 'RU' which is the list of the languages.
   Then Verify the language has changed.