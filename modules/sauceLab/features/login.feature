Feature: Login Page screen

  As an automation engineer
  I want to test the login screen features
  So that it I can deliver the bug free product.

  Background:
    Given I Launch the browser
    When I Open the saucedemo website
    Then The login portal has been opened

  @Login
  Scenario: Login with valid credentials
    Given I provide the username "standard_user" and password "secret_sauce"
    When I click on the Login button
    Then Validate login is successful

  @invalidlogin
  Scenario: Login with invalid credentials
    Given I provide the username "locked_out_user" and password "secret_sauce"
    When I click on the Login button
    Then Validate login is successful

#  @users
#  Scenario Outline: Validate different users
#    Given I provide the username "<username>" and password "<password>"
#    When I click on the Login button
#    Then Validate login is successful
#    And Close the browser
#
#    Examples:
#      | username        | password     |
#      | standard_user   | secret_sauce |
#      | locked_out_user | secret_sauce |
#      | problem_user    | secret_sauce |