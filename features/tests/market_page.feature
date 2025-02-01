Feature: Test Scenarios to test market page.

  Scenario:  User can open market tab and go through the pagination
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on 'Market' at the left side menu.
     Then Verify the Market page opens.
     When Go to the final page using pagination.
     And Go to the first page using pagination.

  Scenario: User can open market tab and filter by developers option
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on 'Market' at the left side menu.
     Then Verify the Market page opens.
     When Click on Developers filter at the top of the page.
     Then Verify all cards has the license tag.


  Scenario: User can open market tab and add company option
     Given Open the main page https://soft.reelly.io
     When Log in to the page.
     And Click on 'Market' at the left side menu.
     Then Verify the Market page opens.
     When Click on 'Add Company' button.
     Then Verify the 'Add Company' page opens.
     And Verify the button 'Publish my company' is available.
