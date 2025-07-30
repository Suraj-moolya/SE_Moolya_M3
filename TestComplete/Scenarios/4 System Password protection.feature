Feature: 4 System Password protection

@TC_EPE_SS_0013
Scenario Outline: Set and enable System Access Password while creating System
When I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'
Then verify context menu items System Explorer Node in system explorer
When I selected Create System in context menu with password
And I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser>'
Examples:
  | SlNo. | project browser           | New Password box1   | Confirm Password box2       |
  | 1     | Create System (Completed) | Password$$Mooly@123 | Confirm Password$$Mooly@123 |
  
@TC_EPE_SS_0014
Scenario Outline: Enable System Access Password from Properties
When I Right Click on nodes System Explorer Node in system explorer as 'System_3'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Close the Tab by Clicking on Close as '<identifier>'
And I Perform action on the Folder by Clicking on '<button>' in Topology Explorer

Examples:
  | SlNo. | context menu | options                      | identifier | button          |
  | 1     | Properties   | System Access Password$$True | Properties | System_3$$Close |
  
@TC_EPE_SS_0014
Scenario Outline: Enable System Access Password from Properties system2
When I Right Click on nodes System Explorer Node in system explorer as 'System_2'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Close the Tab by Clicking on Close as '<identifier>'
And I Perform action on the Folder by Clicking on '<button>' in Topology Explorer

Examples:
  | SlNo. | context menu | options                      | identifier | button          |
  | 1     | Properties   | System Access Password$$True | Properties | System_3$$Close |
  
  
@TC_EPE_SS_0015
Scenario Outline: Set System Access Password
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
And I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser>'
Examples:
  | SlNo. | Systems Explorer | MainToolBar1                   | New Password box1   | Confirm Password box2       | project browser             |
  | 1     | System_3         | Open Topology Explorer (Alt+T) | Password$$Mooly@123 | Confirm Password$$Mooly@123 | Update System_3 (Completed) |
  
  
@TC_EPE_SS_0016
Scenario Outline: Check the Verify Password dialog box
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Enter the password that is set'
When I Enter Controller Password deploy screen TE Confirm Password box in topology as '<Password box>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window>'
Examples:
  | SlNo. | Systems Explorer | MainToolBar1                   | Password box | Modal dialog window |
  | 1     | System_3         | Open Topology Explorer (Alt+T) | Mooly@123    | OK                  |