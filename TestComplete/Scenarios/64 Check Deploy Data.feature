Feature: 64 Check Deploy Data

@TC_EPE_TE_CN_0032
@test002
Scenario Outline: Check Deploy Data
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window2>'
And I Select deploy data from selection grid TE deploy data selection grid in topology
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window3>'
#Then Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 14>'
When I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 15>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel6>'

@Check_Deploy_Data__192.168.33.4__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | Modal dialog window2 | Modal dialog window3 | Modal Dialog Window 14                | Modal Dialog Window 15                    | Notification Pannel6    |
  | 1     | M580_Standalone | Deploy Data             | 192.168.33.4         | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |

@Check_Deploy_Data__182.179.243.21__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | Modal dialog window2 | Modal dialog window3 | Modal Dialog Window 14                | Modal Dialog Window 15                    | Notification Pannel6    |
  | 1     | M580_Standalone | Deploy Data             | 182.179.243.21       | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |

@Check_Deploy_Data__182.233.63.1__M580_Standalone3
Examples:
  | SlNo. | Controller       | Topology Explorer Tree1 | Modal dialog window2 | Modal dialog window3 | Modal Dialog Window 14                | Modal Dialog Window 15                    | Notification Pannel6    |
  | 1     | M580_Standalone3 | Deploy Data             | 182.233.63.1         | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |
  
@Check_Deploy_Data__182.233.63.8__M580_Standalone3
Examples:
  | SlNo. | Controller       | Topology Explorer Tree1 | Modal dialog window2 | Modal dialog window3 | Modal Dialog Window 14                | Modal Dialog Window 15                    | Notification Pannel6    |
  | 1     | M580_Standalone3 | Deploy Data             | 182.233.63.8         | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |

@Check_Deploy_Data__182.233.63.8__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | Modal dialog window2 | Modal dialog window3 | Modal Dialog Window 14                | Modal Dialog Window 15                    | Notification Pannel6    |
  | 1     | M580_Standalone | Deploy Data             | 182.233.63.8         | OK                   | MessageBox$$modaldialogwindow1textbox | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Data (Completed) |


