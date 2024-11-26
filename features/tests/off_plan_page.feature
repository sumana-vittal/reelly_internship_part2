Feature:Test Scenarios for Off-plan Page

  Scenario: User can open the off plan page and go through the pagination
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    When Go to the final page using the pagination button.
    And Go back to the first page using the pagination button.