Feature: 31 Enable system password in SE and open controller in TE, set PW for controller and open it

@TC_EPE_TE_0005a
Scenario Outline: Open controller in TE, set PW for controller and open it - Set PW
When I Enter Controller Password TE New Password box in topology as '<New Password box1>'
And I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'
And I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
And I Click button Message Window Modification popup in message box as '<Modification popup3>'

Examples:
  | SlNo. | New Password box1    | Confirm Password box2        | Modification popup3 |
  | 1     | Password$$Moolya@123 | Confirm Password$$Moolya@123 | OK                  |


@TC_EPE_TE_0005b
Scenario Outline: Deploy the controller after enabling the password
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Enter the application password that has been set for the engine'
When I Enter Controller Password deploy screen TE Confirm Password box in topology as '<Password box3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Password box3 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | project browser2                 | Modal dialog window 16                    |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Moolya@123    | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 192.168.33.4         | Deploy Built Project (Completed) | MessageBox$$modaldialogwindow1textbox$$OK |



@TC_EPE_TE_0005b
Scenario Outline: Enter controller password
When I Enter Controller Password deploy screen TE Confirm Password box in topology as '<Password box3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Password box3 | Executables dropdown3                                     | Modal dialog window4 | project browser2                 |
  | 1     | Moolya@123    | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Deploy Built Project (Completed) |