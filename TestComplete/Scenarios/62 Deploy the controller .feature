﻿Feature: 62 Deploy the controller 

@TC_EPE_TE_CN_0030
@test001
Scenario Outline: Deploy the controller after disabling the password
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I select start engine checkbox in in topology
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_the_controller_after_disabling_the_password__192.168.33.4__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 192.168.33.4         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |

@Deploy_the_controller_after_disabling_the_password__182.179.243.21__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.179.243.21       | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
