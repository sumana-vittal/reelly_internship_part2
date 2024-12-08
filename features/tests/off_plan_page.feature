Feature:Test Scenarios for Off-plan Page

  Scenario: User can open the off plan page and go through the pagination
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    When Go to the final page using the pagination button.
    And Go back to the first page using the pagination button.

  Scenario: User can filter the off plan products by Unit price range
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    When Filter the projects by price range from 1200000 to 2000000 AED.
    Then Verify the price in all cards is in the range (1200000 - 2000000).