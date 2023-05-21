Feature: Dashboard faeture

  Background:
    Given I Launch the browser
    When I Open the saucedemo website
    Then The login portal has been opened

  @dashboardLogin
  Scenario: Test the dashboard products
    Given I provide the username "standard_user" and password "secret_sauce"
    When I click on the Login button
    Then Validate login is successful

