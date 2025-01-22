Feature: 78 Open refine online and check the build and deploy functionality

@TC_EPE_WS_0011
@test001
Scenario Outline: Open refine online and check the build and deploy functionality
When I selected Build and Deploy Changes in control expert
And I selected List of modified Yes button CE in dialog ce
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel2>'

Examples:
  | SlNo. | Modal dialog window1 | Notification Pannel2                 |
  | 1     | OK                   | Build and Deploy Changes (Completed) |


#Total No. of Test Cases :1


@TC_EPE_WS_0011a
@test001
Scenario Outline: Open refine online
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window5 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                      |
  | 1     | Workstation_1 | Control      | Refine Online           | 127.0.0.1:502        | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Open Refine Online Editor (Completed) |


@TC_EPE_WS_0011b
@test000
Scenario Outline: Navigate Through Project Browser
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
@Double_click_on_PLC_Bus_EIO 
Examples:
  | SlNo. | Project Browser RO1                    |
  | 1     | Programs$$Tasks$$MAST$$Logic$$System_1 |
  
@Double_click_on_Networks_Ethernet_2
Examples:
  | SlNo. | Project Browser RO1                 |
  | 1     | Communication$$Networks$$Ethernet_2 |
  
  
@TC_EPE_WS_0011c
Scenario Outline: Close Refine online window and yes on popup
When I selected Close Refine Offline in refine offline
#And I click modal dialog window project browser in project explorer as '<Button>'
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | Button | container dock3                        |
  | 1     | Yes    | Close Refine Online Editor (Completed) |
  

@TC_EPE_WS_0011d
Scenario Outline: Close tab items EC main screen
When I Close tab items EC main screen in engineering client as 'System_1'
And I wait in seconds Refine online window in refine offline

Examples:
  | SlNo. |
  | 1     |
  

@TC_EPE_WS_0011
@test001
Scenario Outline: Open refine online and check the build and deploy and click on deploy in pop up 
When I selected Build and Deploy Changes in control expert
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel2>'

Examples:
  | SlNo. | Modal dialog window1 | Notification Pannel2                 |
  | 1     | Deploy               | Build and Deploy Changes (Completed) |

