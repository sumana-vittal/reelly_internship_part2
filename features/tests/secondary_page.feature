Feature: Test Scenarios for the Secondary Page

  Scenario:  User can open the Secondary deals page and go through the pagination
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on Secondary option at the left side menu.
      Then Verify the Secondary page opens.
      And Go to the final page using the pagination button.
      And Go back to the first page using the pagination button.

  Scenario: User can filter the Secondary deals by "want to sell" option
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on Secondary option at the left side menu.
      Then Verify the Secondary page opens.
      When Click on Filters.
      And Filter the products by 'want to sell'.
      And Click on Apply Filter.
      Then Verify all cards have 'for sale' tag.

  Scenario: User can filter the Secondary deals by “want to buy” option
      Given Open the main page https://soft.reelly.io
      When Log in to the page.
      And Click on Secondary option at the left side menu.
      Then Verify the Secondary page opens.
      When Click on Filters.
      And Filter the products by 'want to buy'.
      And Click on Apply Filter.
      Then Verify all cards have 'Want to buy' tag.