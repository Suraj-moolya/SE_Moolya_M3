Feature: Logout for System server and Login

@TC_EPE_AS_0009
@test001
Scenario Outline: Logout for System server
When I click on Username dropdown
And I click on menuItem option from usericon as '<param>'
Then verify text in system server console Console in server console as '<Console1>'
Examples:
  | SlNo. | Console1              | param   |
  | 1     | A user was logged off | Log Out |
  
  
@TC_EPE_AS_0010
@test001
Scenario Outline: Click on Username Icon and select Login
When I click on Username dropdown
And I click on menuItem option from usericon as '<param>'
Examples:
  | SlNo. | param  |
  | 1     | Log In |
  
@TC_EPE_AS_0010
@test001
Scenario Outline: Click on Username Icon and select Lock
When I click on Username dropdown
And I click on menuItem option from usericon as '<param>'
Examples:
  | SlNo. | param |
  | 1     | Lock  |
  
  
  
#When I click on Username dropdown
#And I click on Login option