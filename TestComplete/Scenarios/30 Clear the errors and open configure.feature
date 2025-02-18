Feature: 30 Clear the errors and open configure

@TC_EPE_TE_0004
Scenario Outline: Clear the errors and open configure.
When I click '<menu1>' in Tool Bar
And I click '<menu_item1>' in Tool Bar popup window
Then Verify_error_messages_in_Console OutputWindowPanel in topology as '<OutputWindowPanel1>'


Examples:
  | SlNo.  | menu_item1          | menu1 | OutputWindowPanel1 |
  | 1      | Rebuild All Project | Build | 0 Error            |