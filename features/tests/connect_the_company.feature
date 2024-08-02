Feature:Scenario to Test Connect the Company button.

  Scenario: Verify right page opens when connect company is clicked
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on 'Connect the company'
      And Switch the new tab.
      Then Verify the right tab opens.