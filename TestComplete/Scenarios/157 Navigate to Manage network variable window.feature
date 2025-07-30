Feature: 157 Navigate to Manage network variable window

@TC_EPE_PE_CP_0041
@test0041
Scenario Outline: Navigate to Manage network variable window and check if the network variables are available
When I RClick control project browser project browser in project explorer as '<projectBrowser1>'
And I Select context menu item EC project browser in project explorer as '<projectBrowser2>'
And I Verify if the Network Variables are available as '<variables>'
Then I selected Ok in Manage Network Variable Window 
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2          | variables           |
  | 1     | ControlProject_2 | Manage Network Variables | guna$$guna2$$guna3  |