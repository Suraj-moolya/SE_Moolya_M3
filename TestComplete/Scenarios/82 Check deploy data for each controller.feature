﻿Feature: 82 Check deploy data for each controller

@TC_EPE_WS_0016
@test001
Scenario Outline: Check deploy data for each controller
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 14>'
When I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel6>'


Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window4 | Modal Dialog Window 14                | Modal Dialog Window 16                    | project browser2        |
  | 1     | Workstation_1 | Control      | Deploy Data             | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |
