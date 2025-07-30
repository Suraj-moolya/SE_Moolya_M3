Feature: 84 Check Redeploy
##Refine Online Test Step To Be Taken Care in Execution Order (TC_EPE_TE_CS_0035)
@TC_EPE_TE_0011
Scenario Outline: Check Redeploy
#When I RClick control project browser project browser in project explorer as '<project browser1>'
#And I Select context menu item EC project browser in project explorer as '<project browser2>'
#And I click modal dialog window project browser in project explorer as '<button>'
#Then Verify Action message in notification pannel container dock in project explorer as '<message>'
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I Right Click on nodes System Explorer Node in system explorer as '<node_name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<option>'
And I click modal dialog window Modal dialog window in message box as '<button>'
And I Click popup button object project browser in project explorer as '<button1>'
Then Verify notification panel message Notification Pannel in message box as '<content>'
Examples:
  | SlNo. | project browser1 | project browser2   | button | message                                           | MainToolBar       | node_name     | context menu | option                 | button1                                   | content                            |
  | 1     | Executable_1     | Generate and Build | OK     | Generate and Build Control Executable (Completed) | Topology Explorer | Workstation_1 | Control      | Re-Deploy Last Project | MessageBox$$modaldialogwindow1textbox$$OK | Re-Deploy Last Project (Completed) |