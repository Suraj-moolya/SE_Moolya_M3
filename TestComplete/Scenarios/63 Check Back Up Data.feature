﻿Feature: 63 Check Back Up Data

@test001
Scenario Outline: Check Backup Data
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window2>'
And I entered backup data description in topology as '<backup data description3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 15>'
When I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel7>'

Examples:
  | SlNo. | Topology Explorer Tree1 | Modal dialog window2 | backup data description3 | Modal dialog window4 | Modal Dialog Window 15                | Modal Dialog Window 16                    | Notification Pannel7     |
  | 1     | Back Up Data            | 192.168.33.4         | M580_Standalone          | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Back Up Data (Completed) |