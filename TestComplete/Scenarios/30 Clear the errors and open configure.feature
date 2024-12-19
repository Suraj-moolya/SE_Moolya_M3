Feature: 30 Clear the errors and open configure

@TC_EPE_TE_0004
Scenario Outline: Clear the errors and open configure.
When I click '<menu1>' in Tool Bar
And I click '<menu_item1>' in Tool Bar popup window
And I wait in seconds Refine online window in refine offline

Examples:
  | SlNo.  | menu_item1          | menu1 |
  | 1      | Rebuild All Project | Build |
  

@TC_EPE_TE_0004a
Scenario Outline: Clear the errors and open configure - verify messages in Console Output Window.
When I wait in seconds Refine online window in refine offline
Then Verify_error_messages_in_Console OutputWindowPanel in topology as '<OutputWindowPanel1>'

Examples:
  | SlNo.         | OutputWindowPanel1 |
  | 1       Build | 0 Error            |
  
  
@TC_EPE_TE_0004b
Scenario Outline: Clear the errors and open configure - verify messages in Console Output Window.
When I wait in seconds Refine online window in refine offline
Then Verify_error_messages_in_Console OutputWindowPanel in topology as '<OutputWindowPanel1>'
Then Verify_error_messages_in_Console OutputWindowPanel in topology as '<OutputWindowPanel2>'


Examples:
  | SlNo. | OutputWindowPanel1                                                                                       | OutputWindowPanel2                                                                                           |
  | 1     | The password for the Firmware is empty or set to default. Please set the password in project properties. | The password for the Data Storage is empty or set to default. Please set the password in project properties. |
  