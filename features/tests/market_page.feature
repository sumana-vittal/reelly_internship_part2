Feature: Test Scenarios to test market page.

  Scenario:  User can open market tab and go through the pagination
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on 'Market' at the left side menu.
     Then Verify the Market page opens.
     When Go to the final page using pagination.
     And Go to the first page using pagination.