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

  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    And Verify each product on this page contains a title and picture visible.

  Scenario: User can filter by sale status Out of Stocks
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    When Filter by sale status of 'Out of Stocks'.
    Then Verify each product contains the Out of Stocks tag.

  Scenario: User can open product detail and see three options of visualization
    Given Open the main page https://soft.reelly.io
    When Log in to the page.
    And Click on off plan option at the left side menu.
    Then Verify the off-plan page opens.
    When Click on the first product.
    Then Verify the one of three options of visualization 'architecture', 'interior', 'lobby' is present and are clickable