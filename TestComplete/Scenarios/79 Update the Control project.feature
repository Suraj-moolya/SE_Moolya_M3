Feature: 79 Update the Control project

@TC_EPE_WS_0012
@test002
Scenario Outline: Check Update Project by closing the Refine Online window and clicking on Yes in the update confirmation dialog box
#When I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
When I checked header cb in message box
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window2>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 3>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel4>'

Examples:
  | SlNo. | Modal dialog window1 | Modal dialog window2 | Modal Dialog Window 3                     | Notification Pannel4       | 
  | 1     | Yes                  | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Update Project (Completed) |

#Total No. of Test Cases :1

