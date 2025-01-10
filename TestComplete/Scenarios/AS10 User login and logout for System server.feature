Feature: Logout for System server and Login

@TC_EPE_AS_0009
@test001
Scenario Outline: Logout for System server and Login
When I click on Username dropdown
And I click on Logout option
Then verify text in system server console Console in server console as '<Console1>'
When I click on Username dropdown
And I click on Login option

Examples:
  | SlNo. | Console1              |
  | 1     | A user was logged off |