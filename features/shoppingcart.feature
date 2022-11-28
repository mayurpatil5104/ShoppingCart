Feature: shopping cart

  Background: Common steps
    Given launch the browser
    When open demo web shop homepage
    And Enter username and password
    And click on login

  Scenario: Clicking on shopping cart icon
    When click on shopping cart
    Then Verify that shopping cart is open
    And click on log out

  Scenario: Selecting item & updating cart & other details

    And Select items to add in cart
    And click on shopping cart
    And update the cart
    Then verify item is selected & updated the cart

    And enter discount code
    And click on apply
    Then verify discount code is applied

    And enter gift code
    And click on Add gift card
    Then verify gift card is applied

    And select country from dropdown list
    And enter zip postal code
    And click on estimate shipping
    Then verify estimate shipping details showing

    And click on terms of services checkbox
    Then verify checkbox is selected
    And click on checkout button
    Then verify checkout page is displayed
    And click on log out


  Scenario: Clear the cart
    And click on shopping cart
    And update the cart
    And click on log out


#  Scenario: Entering discount code
#      Given launch the browser
#      When open demo web shop homepage

#    And click on log out


#  Scenario: Entering gift card code
#      Given launch the browser
#      When open demo web shop homepage

#    And click on log out


#  Scenario: Selecting country from dropdown
#      Given launch the browser
#      When open demo web shop homepage

#    And click on log out

#  Scenario: Selecting terms of services & checkout page
#      Given launch the browser
#      When open demo web shop homepage

#    And click on log out

#    Scenario: Click on checkout
##      Given launch the browser
##      When open demo web shop homepage
#      And click on shopping cart
#      And click on checkout button
#      Then verify checkout page is displayed
#      And click on log out





