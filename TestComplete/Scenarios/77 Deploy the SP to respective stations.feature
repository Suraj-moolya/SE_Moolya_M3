Feature: 77 Deploy the SP to respective stations

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy the SP to respective stations
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<action>'
And I click modal dialog window project browser in project explorer as '<action1>'
And I Select '<ip>' in Workstation Deployment Window
And I click modal dialog window project browser in project explorer as '<action1>'
And I click modal dialog window project browser in project explorer as '<action1>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I Click on the '<button>' in Scada properties and Click '<drop_button>'
And I Click on the '<button2>' in Restore project window 
And I Select the '<file_name>' in Backup-Restore window
And I Click on the '<action1>' in Restore project window 
And I Click on the '<button3>' in Restore project window

Examples:
  | SlNo. | context menu | action               | action1 | Modal Dialog Window 16                    | MainToolBar                     | button | drop_button | button2 | file_name                      | button3 | ip           |
  | 1     | Supervision  | Deploy Built Project | OK      | MessageBox$$modaldialogwindow1textbox$$OK | Release Supervision Participant | Backup | Restore     | Browse  | Supervision_1_Executable_1.ctz | Yes     | 192.168.1.66 |
  
  
  

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy SP without Sharing of OPSC
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<action>'
And I click modal dialog window project browser in project explorer as '<action1>'
And I Select '<ip>' in Workstation Deployment Window
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window project browser in project explorer as '<action1>'
And I Check Any of the files to be added in Deployment File Section as '<instance_names>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'

Examples:
  | SlNo. | context menu | action               | action1 | ip            | instance_names | Modal Dialog Window 16                    |
  | 1     | Supervision  | Deploy Built Project | OK      | 192.168.10.87 | Includes       | MessageBox$$modaldialogwindow1textbox$$OK |