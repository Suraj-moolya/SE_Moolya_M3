Feature: 38 Check update project

@TC_EPE_TE_0009
Scenario Outline: Check Update Project from context menu
When I Right Click on nodes System Explorer Node in system explorer as '<node_name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<option>'
And I click modal dialog window Modal dialog window in message box as '<button>'
And I click the '<property>' checkbox in the Update Project window
And I Click popup button object project browser in project explorer as '<button1>'
And I Click popup button object project browser in project explorer as '<button1>'
Then Verify notification panel message Notification Pannel in message box as '<content>'

Examples:
  | SlNo. | node_name     | context menu | option         | button | property | button1                                   | content                    |
  | 1     | Workstation_1 | Control      | Update Project | OK     | System_1 | MessageBox$$modaldialogwindow1textbox$$OK | Update Project (Completed) |