Feature: 61 Check manage password, clear password and forget password

@TC_EPE_TE_CN_0027
@test001
Scenario Outline: Check manage password
When I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'
Then Verify entered Controller Password valid invalid TE New Password box in topology as '<New Password box4>'
And Verify entered Controller Password valid invalid TE Confirm Password box in topology as '<Confirm Password box5>'


Examples:
  | SlNo. | New Password box1            | Confirm Password box2                | Modification popup3 | New Password box4 | Confirm Password box5 |
  | 1     | Password$$Mooly@1            | Confirm Password$$Mooly@1            | OK                  | Password          | Confirm Password      |
  | 2     | Password$$Mooly@wayoftesting | Confirm Password$$Mooly@wayoftesting | OK                  | Password          | Confirm Password      |
  | 3     | Password$$Moolyawa           | Confirm Password$$Moolyawa           | OK                  | Password          | Confirm Password      |
  | 4     | Password$$Moolya@123         | Confirm Password$$Moolya@45          | OK                  | Password          | Confirm Password      |
  | 5     | Password$$Moolya@123         | Confirm Password$$Moolya@123         | OK                  | Password          | Confirm Password      |



@TC_EPE_TE_CN_0028
@test002
Scenario Outline: Check Forgot password
Then Verify forgot password Authentication Code Export popup in message box
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as '<Button>'


Examples:
  | SlNo. | Button |
  | 1     | OK     |


@TC_EPE_TE_CN_0029
@test003
Scenario Outline: Check Clear Password
When I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box1>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup2>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify entered Controller Password valid invalid TE New Password box in topology as '<New Password box3>'


Examples:
  | SlNo. | Confirm Password box1        | Modification popup2 | New Password box3 |
  | 1     | Current Password$$Moolya     | OK                  | Password          |
  | 2     | Current Password$$Moolya@123 | OK                  | Password          |



@TC_EPE_TE_CN_0027a
@test001
Scenario Outline: Select Manage password 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'

Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Manage Password         |
  
  
@TC_EPE_TE_CN_0028a
@test001
Scenario Outline: Select Forgot password 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'

Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Forgot Password        |
  
  
@TC_EPE_TE_CN_0029a
@test001
Scenario Outline: Select Clear Password 
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'

Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 |
  | 1     | M580_Standalone | Clear Password         |
