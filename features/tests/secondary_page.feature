Feature: Test Scenarios for the Secondary Page

  Scenario:  User can open the Secondary deals page and go through the pagination
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on Secondary option at the left side menu.
      Then Verify the Secondary page opens.
      And Go to the final page using the pagination button.
      And Go back to the first page using the pagination button.