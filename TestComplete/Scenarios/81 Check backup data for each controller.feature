Feature: 81 Check backup data for each controller

@TC_EPE_WS_0015
@test001
Scenario Outline: Check backup data for each controller
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item  ECproject browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window2>'
And I entered backup data description in topology as '<backup data description3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 15>'
When I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel7>'

Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window2 | backup data description3 | Modal dialog window4 | Modal Dialog Window 15                | Modal Dialog Window 16                    | Notification Pannel7     |
  | 1     | Workstation_1 | Control      | Back Up Data            | 127.0.0.1:502        | Workstation data backup  | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Back Up Data (Completed) |


@TC_EPE_WS_0015a
@test001
Scenario Outline: Check backup data for each controller - Verify in Project Explorer(PE)
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I Verify backup data PE in project explorer as '<project browser3>'
And I Close modal dialog window

Examples:
  | SlNo. | project browser1 | project browser2         | project browser3 |
  | 1     | M580_Standalone  | Manage Data Backup Files | Workstation_1    |